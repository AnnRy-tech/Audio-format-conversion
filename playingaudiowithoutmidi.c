// The sequence of notes to play
const uint8_t note_sequence[] = {12, 14, 16, 17, 19, 21, 23, 24};
#define SEQUENCE_LENGTH (sizeof(note_sequence) / sizeof(note_sequence[0])) // Evaluates to 8

volatile int8_t sequence_index = -1; // -1 means the music is currently stopped



// Call this ONCE to start the playback loop
void start_music_stream()
{
    sequence_index = 0; // Start at the first note (index 0 -> note 12)
    stream_var = 400;   // 1 second duration
    
    uint8_t current_note = note_sequence[sequence_index];
    Btn_Data_Status[current_note] = 1; // Mark the first note active
}

void music_stream_playback()
{
    // INSTANT BREAK: Shut down immediately if flag drops to 0
    if (first_press_1 == 0)
    {
        if (sequence_index != -1) 
        {
            uint8_t current_note = note_sequence[sequence_index];
            Btn_Data_Status[current_note] = 0; 
            
            sequence_index = -1; // Reset to stopped state
            stream_var = 0;
            // PORTR.OUTCLR = 0x02; // Force clear audio pin here
        }
        return; 
    }

    // Process the active sequence when the 1-second timer hits 0
    if (stream_var == 0 && sequence_index != -1)
    {
        // 1. Turn OFF the note that just finished playing
        uint8_t old_note = note_sequence[sequence_index];
        Btn_Data_Status[old_note] = 0;
        
        // 2. Move to the next index in the array
        sequence_index++;
        
        // 3. Check if we reached the end of the array
        if (sequence_index >= SEQUENCE_LENGTH)
        {
            // If loop condition is still met, restart from the beginning
            if (first_press_1 != 0)
            {
                sequence_index = 0; 
            }
            else
            {
                sequence_index = -1; // Stop completely
            }
        }

        // 4. If we have a valid next note, turn it ON and reset the timer
        if (sequence_index != -1)
        {
            uint8_t new_note = note_sequence[sequence_index];
            Btn_Data_Status[new_note] = 1;
            
            stream_var = 400;    // Reset timer for 1 second
            PORTR.OUTTGL = 0x02; // Toggle pin
        }
    }
}


interrupt [TCF0_OVF_vect] void tcf0_overflow_isr(void) 
{    
   
   if(stream_var != 0)
   {
      stream_var--; // Decrements by 1 every 2.5ms
   }
}
