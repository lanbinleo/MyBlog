---
title: Tap To Midi | 用键盘敲击鼓点生成MIDI文件
tags:
  - Python
  - Music
categories:
  - Coding
abbrlink: '70975104'
date: 2024-03-18 18:10:02
---

## 背景

最近参加了“清澜好声音”需要扒谱一首音乐作为伴奏，沙克负责了旋律部分，将打击乐部分交给了我。由于找不到完美匹配的MIDI文件，于是我自己动手，花了一点时间写了一个能够通过敲击键盘来记录鼓点，并导出为MIDI文件的程序。

## 解决方案

我请ChatGPT编写了一个简单的Python程序，它允许用户通过敲击键盘的空格键来模拟鼓点。程序记录下每次击打的时间点，并将它们转换成MIDI格式。

```python
import mido
from mido import MidiFile, MidiTrack, Message
import keyboard
import time

bpm = 120  # 设置BPM
beats_per_second = bpm / 60

print("Press and hold SPACE to start recording. Release to stop.")

while True:
    try:
        keyboard.wait('space')
        start_time = time.time()
        times = []

        print("Recording... Press SPACE to mark the beat. Press ESC to finish.")

        while True:
            try:
                keyboard.wait('space')
                times.append(time.time() - start_time)
                print("Beat!")
                if keyboard.is_pressed('esc'):
                    break
            except:
                break

        mid = MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)
        track.append(Message('program_change', program=12, time=0))

        last_time = 0
        for t in times:
            ticks = int(mido.second2tick(t - last_time, mid.ticks_per_beat, mido.bpm2tempo(bpm)))
            track.append(Message('note_on', note=36, velocity=64, time=ticks))
            track.append(Message('note_off', note=36, velocity=64, time=0))
            last_time = t

        midi_file_name = "drum_beat.mid"
        mid.save(midi_file_name)
        print(f"MIDI file saved as {midi_file_name}")

        break

    except KeyboardInterrupt:
        break
```

## 代码分析

1. 初始化：首先，我们设置了BPM（每分钟节拍数），然后准备接收用户的输入。

2. 记录鼓点：程序使用`keyboard`库等待用户按下空格键开始录制，并记录每次按键的时间点。

3. 生成MIDI：一旦录制完成，我们将这些时间点转换成MIDI格式。每个时间点被转换成一个鼓点音符（MIDI标准中的36号音符），并根据其在录制中的时间安排在MIDI文件中。

4. 导出MIDI文件：最后，程序将所有的MIDI消息保存到一个轨道中，并将该轨道添加到MIDI文件中。然后将文件保存到本地磁盘。

## 结果

通过使用这个程序，我们可以准确地记录下想要的鼓点，并转换成MIDI文件。如果你有任何需要自定义MIDI鼓点的需求，feel free to try this code!

