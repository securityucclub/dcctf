#!/bin/sh
7z e iic3301.7z
steghide extract -sf 0.wav -p nothingscarvedinstone
steghide extract -sf 1.jpg -p dcctf
steghide extract -sf 2.jpg -p flagpls
cat flag.txt
