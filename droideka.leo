<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="peckj.20180622114918.1" a="E"><vh>@auto droideka.py</vh></v>
<v t="peckj.20180622152459.1" a="E"><vh>Docs</vh>
<v t="peckj.20180622152503.1"><vh>CC implementation</vh></v>
<v t="peckj.20180622152604.1"><vh>Implementation notes</vh></v>
</v>
<v t="peckj.20180622115226.1"><vh>@auto README.md</vh></v>
</vnodes>
<tnodes>
<t tx="peckj.20180622152459.1"></t>
<t tx="peckj.20180622152503.1">MIDI IMPLEMENTATION

Note that most DROID-3 parameters require 8 bit and since MIDI CCs are 7 bit there is an interpreter mode set by CC 16.

CC    Parameter
016    Value interpreter mode:
         CC016 set to 0 (default) =&gt; CC values are doubled [0,2,4,6,8...]
         CC016 set to 1 =&gt; CC values are unchanged [0,1,2,3...]
         CC016 set to 2 =&gt; 128 is added [128,129,130...] - if possible
         CC016 set to 3 =&gt; Sets a matrix controller [0,1,2,3...15] - if possible
020    Mixing structure (filter type and routing):
         Bit 1   = Pre mix DCO1 (1:through filter)
         Bit 2   = Pre mix DCO2 (1:through filter)
         Bit 3   = Post mix DCO1 (1:pass filter)
         Bit 4   = Post mix DCO2 (1:pass filter)
         Bit 5   = Filter mode (0:one filter, 1:two parallel)
         Bit 6+7 = Filter type:
                  Bit 5 is 0: 00=LP 01=BP 10=HP 11=BJ
                  Bit 5 is 1: 00=LP/LP 01=LP/HP 11=HP/HP 10=HP/LP
         Bit 8   = Boost mix
021    Filter cutoff 1
022    Filter cutoff 2 or width depending on the value of CC020 bit 6+7
023    Arpeggio speed
024    DCO2 and envelope 2 step amount [0-7]
025    Various modes:
         Bit 1 = Sync slave mode for DCO 1
         Bit 2 = Legato envelope mode
         Bit 3 = Retrig for DCO 1
         Bit 4 = Retrig for DCO 2
         Bit 5 = Key follow for DCO 1
         Bit 6 = Key follow for DCO 2
         Bit 7 = Envelope 1 loop (w/ fade in and retrig)
         Bit 8 = Envelope 2 loop (free run)
026    DCO1 waveform [0-31] - 8 waveforms - 4 overload modes:
         0-7 = Clip overload
         8-15 = Mirror overload
         16-23 = Zero snap (mute) overload
         24-32 = Wrap overload
027    DCO1 pulse width
028    DCO1 offset
029    DCO1 amplitude
030    DCO1 octave [0-63] - 16 octaves - 4 frequency tuning modes (for CC031):
         0-15 = Fine tuning
         16-31 = Linear tuning
         32-47 = Standard tuning
         48-63 = Wide tuning
031    DCO1 frequency
102    DCO2 waveform [0-31] - 8 waveforms - 4 overload modes:
         0-7 = Clip overload
         8-15 = Mirror overload
         16-23 = Zero snap (mute) overload
         24-32 = Wrap overload
103    DCO2 pulse width
104    DCO2 offset
105    DCO2 amplitude
106    DCO2 octave [0-63] - 16 octaves - 4 frequency tuning modes (for CC107):
         0-15 = Fine tuning
         16-31 = Linear tuning
         32-47 = Standard tuning
         48-63 = Wide tuning
107    DCO2 frequency
108    Envelope 1 attack
109    Envelope 1 attack level
110    Envelope 1 decay
111    Envelope 1 sustain level
112    Envelope 1 release
113    Envelope 1 offset
114    Envelope 2 attack
115    Envelope 2 attack level
116    Envelope 2 decay
117    Envelope 2 sustain level
118    Envelope 2 release
119    Envelope 2 offset
120    MIDI channel [1-16]

</t>
<t tx="peckj.20180622152604.1">CC120 (Midi Channel): not going to implement.  The MIDI Channel control is only to select the channel it's listening on.

Generally: If value &lt;= 127, send CC016 = 1, if value &gt; 127 send CC016 = 2

Step           -&gt; CC024
Arp speed      -&gt; CC023  ** MATRIX
Boost mix      -&gt; CC020 bit 8
Legato         -&gt; CC025 bit 2
Filter routing -&gt; CC020 bits 5/6/7
Flt 1 cutoff   -&gt; CC021  ** MATRIX
Flt 2 cutoff   -&gt; CC022  ** MATRIX

DCO1 wav      -&gt; CC026  ** MATRIX
     dist     -&gt; CC026  ** MATRIX
     pw       -&gt; CC027  ** MATRIX
     freq     -&gt; CC037  ** MATRIX
     tun      -&gt; CC030
     oct      -&gt; CC030
     amp      -&gt; CC029  ** MATRIX
     off      -&gt; CC028  ** MATRIX
     post-mix -&gt; CC020 bit 3
     retrig   -&gt; CC025 bit 3
     kf       -&gt; CC025 bit 5
     sync     -&gt; CC025 bit 1

DCO2 wav      -&gt; CC102  ** MATRIX
     dist     -&gt; CC102  ** MATRIX
     pw       -&gt; CC103  ** MATRIX
     freq     -&gt; CC107  ** MATRIX
     tun      -&gt; CC106
     oct      -&gt; CC106
     amp      -&gt; CC105  ** MATRIX
     off      -&gt; CC104  ** MATRIX
     post-mix -&gt; CC020 bit 4
     retrig   -&gt; CC025 bit 4
     kf       -&gt; CC025 bit 6

Env1 off  -&gt; CC113  ** MATRIX
     att  -&gt; CC108
     lvl  -&gt; CC109
     dec  -&gt; CC110
     sus  -&gt; CC111
     rel  -&gt; CC112
     loop -&gt; CC025 bit 7

Env2 off  -&gt; CC119  ** MATRIX
     att  -&gt; CC114
     lvl  -&gt; CC115
     dec  -&gt; CC116
     sus  -&gt; CC117
     rel  -&gt; CC118
     loop -&gt; CC025 bit 8</t>
</tnodes>
</leo_file>
