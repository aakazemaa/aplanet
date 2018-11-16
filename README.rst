audio/noise mixture
-------------------

This is a commandline utility for generating mixed audio and noise files.
It is required to have valid audio files and the same number of noise files
in two different directories. For simplicity we name audio files with an increasing sequenced of integers (as shown below)
A utility create_noise_files.py creates noise files. However, valid audio wav files needs to
be provided.

How to install:
sudo python setup.py install

How to generate the mixed files:
usage: wavegenerator.py [-h] noisedir audiodir mixeddir SNR

Generate mixed audio noise files

positional arguments:
  noisedir    spcefiy where the noise files are located
  audiodir    spcefiy where the audio files are located
  mixeddir    spcefiy where the output dir for mixed files audio/noise are located
  SNR         spcefiy SNR level

example:

python soundmixture/wavegenerator.py ./data/noise/ ./data/audio/ ./data/mixedaudZorro -30


output:
audio/noise mixed files are:  
./data/mixedaudZorro/mixed_1.wav  
./data/mixedaudZorro/mixed_10.wav  
./data/mixedaudZorro/mixed_2.wav  
./data/mixedaudZorro/mixed_3.wav  
./data/mixedaudZorro/mixed_4.wav  
./data/mixedaudZorro/mixed_5.wav  
./data/mixedaudZorro/mixed_6.wav 
./data/mixedaudZorro/mixed_7.wav  
./data/mixedaudZorro/mixed_8.wav  
./data/mixedaudZorro/mixed_9.wav  


Input noise files are located at:
ls -1 data/noise/
noise1.wav
noise10.wav
noise2.wav
noise3.wav
noise4.wav
noise5.wav
noise6.wav
noise7.wav
noise8.wav
noise9.wav


Input audio files are located at:
ls -1 data/audio/
1.wav
10.wav
2.wav
3.wav
4.wav
5.wav
6.wav
7.wav
8.wav
9.wav

Note: soundmixture.log will contain information about latest conversion date and can be expanded for more details.
