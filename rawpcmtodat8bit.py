# 8 BIT


from google.colab import files
import numpy as np
import os

uploaded = files.upload()
fname = next(iter(uploaded))


pcm = np.fromfile(fname, dtype=np.int8)


print("min:", pcm.min(), "max:", pcm.max())
print("first 20 samples:", pcm[:20])

out = os.path.splitext(fname)[0] + ".dat"


np.savetxt(
    out,
    pcm.reshape(1, -1),
    delimiter=",",
    fmt="%d"
)

files.download(out)
