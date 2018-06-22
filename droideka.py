#!/usr/bin/env python2

import Tkinter as tk

root = tk.Tk()
root.title("Droideka")

# MAIN controls
main_frame = tk.LabelFrame(root, text="MAIN", padx=5, pady=5)
main_frame.grid(row=0, column=0, sticky=tk.N)
w = tk.Label(main_frame, text="MIDI Channel")
w.grid(row=0, column=0, sticky=tk.W)
midi_channel = tk.Spinbox(main_frame, from_=1, to=16)
midi_channel.grid(row=0,column=1, sticky=tk.E)
w = tk.Label(main_frame, text="Step")
w.grid(row=1, column=0, sticky=tk.W)
step = tk.Scale(main_frame, from_=0, to=7, orient=tk.HORIZONTAL)
step.grid(row=1, column=1, sticky=tk.E)
w = tk.Label(main_frame, text="Arp Speed")
w.grid(row=2, column=0, sticky=tk.W)
arp = tk.Scale(main_frame, from_=0, to=255, orient=tk.HORIZONTAL)
arp.grid(row=2, column=1, sticky=tk.E)
fltr_boost_var = tk.IntVar(main_frame)
fltr_boost_var.set(0)
fltr_boost = tk.Checkbutton(main_frame, text="Boost mix", variable=fltr_boost_var)
fltr_boost.grid(row=3, column=0, sticky=tk.W)
legato_var = tk.IntVar(main_frame)
legato_var.set(0)
legato = tk.Checkbutton(main_frame, text="Legato", variable=legato_var)
legato.grid(row=3, column=1, sticky=tk.W)


# FLTR controls
fltr_frame = tk.LabelFrame(root, text="FLTR", padx=5, pady=5)
fltr_frame.grid(row=1, column=0, sticky=tk.N)
w = tk.Label(fltr_frame, text="Filter Routing")
w.grid(row=0, column=0, sticky=tk.W)
fltr_routing_var = tk.StringVar(fltr_frame)
fltr_routing_var.set("Off")
fltr_routing = tk.OptionMenu(fltr_frame, fltr_routing_var, "Off", "DCO1 -> LP", "DCO1 -> HP", "DCO1 -> BP", "DCO1 -> BR",
                                                                  "DCO2 -> LP", "DCO2 -> HP", "DCO2 -> BP", "DCO2 -> BR",
                                                                  "DCO1+2 -> LP", "DCO1+2 -> HP", "DCO1+2 -> BP", "DCO1+2 -> BR",
                                                                  "DCO1 -> LP1/DCO2 ->LP2", "DCO1 -> LP/DCO2 -> HP", 
                                                                  "DCO1 -> HP/DCO2 -> LP", "DCO1 -> HP1/DCO2 ->HP2")
fltr_routing.grid(row=0, column=1, sticky=tk.E)
w = tk.Label(fltr_frame, text="Flt 1 cutoff")
w.grid(row=2, column=0, sticky=tk.W)
fltr_cut = tk.Scale(fltr_frame, from_=0, to=255, orient=tk.HORIZONTAL)
fltr_cut.grid(row=2, column=1, sticky=tk.E)
w = tk.Label(fltr_frame, text="Flt2 cutoff/Flt1 width")
w.grid(row=3, column=0, sticky=tk.W)
fltr_wid = tk.Scale(fltr_frame, from_=0, to=255, orient=tk.HORIZONTAL)
fltr_wid.grid(row=3, column=1, sticky=tk.E)


# DCO1 controls
dco1_frame = tk.LabelFrame(root, text="DCO1", padx=5, pady=5)
dco1_frame.grid(row=0, rowspan=2, column=1, sticky=tk.N)

w = tk.Label(dco1_frame, text="Waveform")
w.grid(row=0, column=0, sticky=tk.W)
dco1_waveform_var = tk.StringVar(dco1_frame)
dco1_waveform_var.set("Saw-Up")
dco1_waveform = tk.OptionMenu(dco1_frame, dco1_waveform_var, "Saw-Up", "Saw-Down", "Square", "Triangle", "White Noise", "S&H Random", "Digital", "Silence")
dco1_waveform.grid(row=0, column=1, sticky=tk.E)

w = tk.Label(dco1_frame, text="Distortion Mode")
w.grid(row=1, column=0, sticky=tk.W)
dco1_distortion_var = tk.StringVar(dco1_frame)
dco1_distortion_var.set("Clipping")
dco1_distortion = tk.OptionMenu(dco1_frame, dco1_distortion_var, "Clipping", "Mirror", "Zero-snap", "Wrap")
dco1_distortion.grid(row=1, column=1, sticky=tk.E)

w = tk.Label(dco1_frame, text="Pulsewidth")
w.grid(row=2, column=0, sticky=tk.W)
dco1_pw = tk.Scale(dco1_frame, from_=0, to=255, orient=tk.HORIZONTAL)
dco1_pw.set(128)
dco1_pw.grid(row=2, column=1, sticky=tk.E)

w = tk.Label(dco1_frame, text="Frequency")
w.grid(row=3, column=0, sticky=tk.W)
dco1_frequency = tk.Scale(dco1_frame, from_=0, to=255, orient=tk.HORIZONTAL)
dco1_frequency.set(128)
dco1_frequency.grid(row=3, column=1, sticky=tk.E)

w = tk.Label(dco1_frame, text="Tuning Mode")
w.grid(row=4, column=0, sticky=tk.W)
dco1_tuning_var = tk.StringVar(dco1_frame)
dco1_tuning_var.set("Fine")
dco1_tuning = tk.OptionMenu(dco1_frame, dco1_tuning_var, "Fine", "Linear", "Standard", "Wide")
dco1_tuning.grid(row=4, column=1, sticky=tk.E)

w = tk.Label(dco1_frame, text="Octave")
w.grid(row=5, column=0, sticky=tk.W)
dco1_octave = tk.Scale(dco1_frame, from_=0, to=15, orient=tk.HORIZONTAL)
dco1_octave.grid(row=5, column=1, sticky=tk.E)

w = tk.Label(dco1_frame, text="Amplitude")
w.grid(row=6, column=0, sticky=tk.W)
dco1_amp = tk.Scale(dco1_frame, from_=0, to=255, orient=tk.HORIZONTAL)
dco1_amp.grid(row=6, column=1, sticky=tk.E)

w = tk.Label(dco1_frame, text="Offset")
w.grid(row=7, column=0, sticky=tk.W)
dco1_offset = tk.Scale(dco1_frame, from_=0, to=255, orient=tk.HORIZONTAL)
dco1_offset.set(128)
dco1_offset.grid(row=7, column=1, sticky=tk.E)

dco1_syncslave_var = tk.IntVar(dco1_frame)
dco1_syncslave_var.set(0)
dco1_syncslave = tk.Checkbutton(dco1_frame, text="Sync-slave", variable=dco1_syncslave_var)
dco1_syncslave.grid(row=9, column=1, sticky=tk.W)

dco1_retrig_var = tk.IntVar(dco1_frame)
dco1_retrig_var.set(0)
dco1_retrig = tk.Checkbutton(dco1_frame, text="Retrig", variable=dco1_retrig_var)
dco1_retrig.grid(row=8, column=1, sticky=tk.W)

dco1_keyfollow_var = tk.IntVar(dco1_frame)
dco1_keyfollow_var.set(0)
dco1_keyfollow = tk.Checkbutton(dco1_frame, text="Key-follow", variable=dco1_keyfollow_var)
dco1_keyfollow.grid(row=9, column=0, sticky=tk.W)

dco1_postmix_var = tk.IntVar(dco1_frame)
dco1_postmix_var.set(0)
dco1_postmix = tk.Checkbutton(dco1_frame, text="Post-filter mix", variable=dco1_postmix_var)
dco1_postmix.grid(row=8, column=0, sticky=tk.W)

# DCO2 controls
dco2_frame = tk.LabelFrame(root, text="DCO2", padx=5, pady=5)
dco2_frame.grid(row=0, rowspan=2, column=2, sticky=tk.N)

w = tk.Label(dco2_frame, text="Waveform")
w.grid(row=0, column=0, sticky=tk.W)
dco2_waveform_var = tk.StringVar(dco2_frame)
dco2_waveform_var.set("Saw-Up")
dco2_waveform = tk.OptionMenu(dco2_frame, dco2_waveform_var, "Saw-Up", "Saw-Down", "Square", "Triangle", "White Noise", "S&H Random", "Digital", "Silence")
dco2_waveform.grid(row=0, column=1, sticky=tk.E)

w = tk.Label(dco2_frame, text="Distortion Mode")
w.grid(row=1, column=0, sticky=tk.W)
dco2_distortion_var = tk.StringVar(dco2_frame)
dco2_distortion_var.set("Clipping")
dco2_distortion = tk.OptionMenu(dco2_frame, dco2_distortion_var, "Clipping", "Mirror", "Zero-snap", "Wrap")
dco2_distortion.grid(row=1, column=1, sticky=tk.E)

w = tk.Label(dco2_frame, text="Pulsewidth")
w.grid(row=2, column=0, sticky=tk.W)
dco2_pw = tk.Scale(dco2_frame, from_=0, to=255, orient=tk.HORIZONTAL)
dco2_pw.set(128)
dco2_pw.grid(row=2, column=1, sticky=tk.E)

w = tk.Label(dco2_frame, text="Frequency")
w.grid(row=3, column=0, sticky=tk.W)
dco2_frequency = tk.Scale(dco2_frame, from_=0, to=255, orient=tk.HORIZONTAL)
dco2_frequency.set(128)
dco2_frequency.grid(row=3, column=1, sticky=tk.E)

w = tk.Label(dco2_frame, text="Tuning Mode")
w.grid(row=4, column=0, sticky=tk.W)
dco2_tuning_var = tk.StringVar(dco2_frame)
dco2_tuning_var.set("Fine")
dco2_tuning = tk.OptionMenu(dco2_frame, dco2_tuning_var, "Fine", "Linear", "Standard", "Wide")
dco2_tuning.grid(row=4, column=1, sticky=tk.E)

w = tk.Label(dco2_frame, text="Octave")
w.grid(row=5, column=0, sticky=tk.W)
dco2_octave = tk.Scale(dco2_frame, from_=0, to=15, orient=tk.HORIZONTAL)
dco2_octave.grid(row=5, column=1, sticky=tk.E)

w = tk.Label(dco2_frame, text="Amplitude")
w.grid(row=6, column=0, sticky=tk.W)
dco2_amp = tk.Scale(dco2_frame, from_=0, to=255, orient=tk.HORIZONTAL)
dco2_amp.grid(row=6, column=1, sticky=tk.E)

w = tk.Label(dco2_frame, text="Offset")
w.grid(row=7, column=0, sticky=tk.W)
dco2_offset = tk.Scale(dco2_frame, from_=0, to=255, orient=tk.HORIZONTAL)
dco2_offset.set(128)
dco2_offset.grid(row=7, column=1, sticky=tk.E)

dco2_retrig_var = tk.IntVar(dco2_frame)
dco2_retrig_var.set(0)
dco2_retrig = tk.Checkbutton(dco2_frame, text="Retrig", variable=dco2_retrig_var)
dco2_retrig.grid(row=8, column=1, sticky=tk.W)

dco2_keyfollow_var = tk.IntVar(dco2_frame)
dco2_keyfollow_var.set(0)
dco2_keyfollow = tk.Checkbutton(dco2_frame, text="Key-follow", variable=dco2_keyfollow_var)
dco2_keyfollow.grid(row=9, column=0, sticky=tk.W)

dco2_postmix_var = tk.IntVar(dco2_frame)
dco2_postmix_var.set(0)
dco2_postmix = tk.Checkbutton(dco2_frame, text="Post-filter mix", variable=dco2_postmix_var)
dco2_postmix.grid(row=8, column=0, sticky=tk.W)

# ENV1 controls
env1_frame = tk.LabelFrame(root, text="ENV1", padx=5, pady=5)
env1_frame.grid(row=0, rowspan=2, column=3, sticky=tk.N)

w = tk.Label(env1_frame, text="Offset")
w.grid(row=0, column=0, sticky=tk.W)
env1_offset = tk.Scale(env1_frame, from_=0, to=255, orient=tk.HORIZONTAL)
env1_offset.grid(row=0, column=1, sticky=tk.E)

w = tk.Label(env1_frame, text="Attack")
w.grid(row=1, column=0, sticky=tk.W)
env1_attack = tk.Scale(env1_frame, from_=0, to=255, orient=tk.HORIZONTAL)
env1_attack.grid(row=1, column=1, sticky=tk.E)

w = tk.Label(env1_frame, text="Level")
w.grid(row=2, column=0, sticky=tk.W)
env1_level = tk.Scale(env1_frame, from_=0, to=255, orient=tk.HORIZONTAL)
env1_level.grid(row=2, column=1, sticky=tk.E)

w = tk.Label(env1_frame, text="Decay")
w.grid(row=3, column=0, sticky=tk.W)
env1_decay = tk.Scale(env1_frame, from_=0, to=255, orient=tk.HORIZONTAL)
env1_decay.grid(row=3, column=1, sticky=tk.E)

w = tk.Label(env1_frame, text="Sustain")
w.grid(row=4, column=0, sticky=tk.W)
env1_sustain = tk.Scale(env1_frame, from_=0, to=255, orient=tk.HORIZONTAL)
env1_sustain.grid(row=4, column=1, sticky=tk.E)

w = tk.Label(env1_frame, text="Release")
w.grid(row=5, column=0, sticky=tk.W)
env1_release = tk.Scale(env1_frame, from_=0, to=255, orient=tk.HORIZONTAL)
env1_release.grid(row=5, column=1, sticky=tk.E)

env1_freerun_var = tk.IntVar(env1_frame)
env1_freerun_var.set(0)
env1_freerun = tk.Checkbutton(env1_frame, text="Loop with fade/retrig", variable=env1_freerun_var)
env1_freerun.grid(row=6, column=0, sticky=tk.W)

# ENV2 controls
env2_frame = tk.LabelFrame(root, text="ENV2", padx=5, pady=5)
env2_frame.grid(row=0, rowspan=2, column=4, sticky=tk.N)

w = tk.Label(env2_frame, text="Offset")
w.grid(row=0, column=0, sticky=tk.W)
env2_offset = tk.Scale(env2_frame, from_=0, to=255, orient=tk.HORIZONTAL)
env2_offset.grid(row=0, column=1, sticky=tk.E)

w = tk.Label(env2_frame, text="Attack")
w.grid(row=1, column=0, sticky=tk.W)
env2_attack = tk.Scale(env2_frame, from_=0, to=255, orient=tk.HORIZONTAL)
env2_attack.grid(row=1, column=1, sticky=tk.E)

w = tk.Label(env2_frame, text="Level")
w.grid(row=2, column=0, sticky=tk.W)
env2_level = tk.Scale(env2_frame, from_=0, to=255, orient=tk.HORIZONTAL)
env2_level.grid(row=2, column=1, sticky=tk.E)

w = tk.Label(env2_frame, text="Decay")
w.grid(row=3, column=0, sticky=tk.W)
env2_decay = tk.Scale(env2_frame, from_=0, to=255, orient=tk.HORIZONTAL)
env2_decay.grid(row=3, column=1, sticky=tk.E)

w = tk.Label(env2_frame, text="Sustain")
w.grid(row=4, column=0, sticky=tk.W)
env2_sustain = tk.Scale(env2_frame, from_=0, to=255, orient=tk.HORIZONTAL)
env2_sustain.grid(row=4, column=1, sticky=tk.E)

w = tk.Label(env2_frame, text="Release")
w.grid(row=5, column=0, sticky=tk.W)
env2_release = tk.Scale(env2_frame, from_=0, to=255, orient=tk.HORIZONTAL)
env2_release.grid(row=5, column=1, sticky=tk.E)

env2_freerun_var = tk.IntVar(env2_frame)
env2_freerun_var.set(0)
env2_freerun = tk.Checkbutton(env2_frame, text="Loop free-run", variable=env2_freerun_var)
env2_freerun.grid(row=6, column=0, sticky=tk.W)



root.mainloop()


