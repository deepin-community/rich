expected = '\x1b[1mTraceback\x1b[0m \x1b[2m(most recent call last):\x1b[0m\n\x1b[34m╭──────────────────────────────────────────────────────────────────────────────────────╮\x1b[0m\n\x1b[34m│\x1b[0m File \x1b[32m"test_traceback.py"\x1b[0m, line \x1b[1;36m24\x1b[0m, in \x1b[33mget_exception\x1b[0m                                  \x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m21 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m    \x1b[0m\x1b[38;2;102;217;239;48;2;39;40;34mtry\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m:\x1b[0m\x1b[48;2;39;40;34m                                                                       \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m22 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m        \x1b[0m\x1b[38;2;102;217;239;48;2;39;40;34mtry\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m:\x1b[0m\x1b[48;2;39;40;34m                                                                   \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m23 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m            \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34mfoo\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m(\x1b[0m\x1b[38;2;174;129;255;48;2;39;40;34m0\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m)\x1b[0m\x1b[48;2;39;40;34m                                                             \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[38;2;101;102;96;48;2;39;40;34m❱ \x1b[0m\x1b[1;38;2;227;227;221;48;2;39;40;34m24 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m        \x1b[0m\x1b[38;2;102;217;239;48;2;39;40;34mexcept\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m:\x1b[0m\x1b[48;2;39;40;34m                                                                \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m25 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m            \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34mfoobarbaz\x1b[0m\x1b[48;2;39;40;34m                                                          \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m26 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m    \x1b[0m\x1b[38;2;102;217;239;48;2;39;40;34mexcept\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m:\x1b[0m\x1b[48;2;39;40;34m                                                                    \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m27 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m        \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34mtb\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m \x1b[0m\x1b[38;2;249;38;114;48;2;39;40;34m=\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34mTraceback\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m(\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m)\x1b[0m\x1b[48;2;39;40;34m                                                       \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m File \x1b[32m"test_traceback.py"\x1b[0m, line \x1b[1;36m20\x1b[0m, in \x1b[33mfoo\x1b[0m                                            \x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m17 \x1b[0m\x1b[48;2;39;40;34m                                                                               \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m18 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m    \x1b[0m\x1b[38;2;102;217;239;48;2;39;40;34mdef\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m \x1b[0m\x1b[38;2;166;226;46;48;2;39;40;34mfoo\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m(\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34ma\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m)\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m:\x1b[0m\x1b[48;2;39;40;34m                                                                \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m19 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m        \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34mbar\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m(\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34ma\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m)\x1b[0m\x1b[48;2;39;40;34m                                                                 \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[38;2;101;102;96;48;2;39;40;34m❱ \x1b[0m\x1b[1;38;2;227;227;221;48;2;39;40;34m20 \x1b[0m\x1b[48;2;39;40;34m                                                                               \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m21 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m    \x1b[0m\x1b[38;2;102;217;239;48;2;39;40;34mtry\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m:\x1b[0m\x1b[48;2;39;40;34m                                                                       \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m22 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m        \x1b[0m\x1b[38;2;102;217;239;48;2;39;40;34mtry\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m:\x1b[0m\x1b[48;2;39;40;34m                                                                   \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m23 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m            \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34mfoo\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m(\x1b[0m\x1b[38;2;174;129;255;48;2;39;40;34m0\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m)\x1b[0m\x1b[48;2;39;40;34m                                                             \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m File \x1b[32m"test_traceback.py"\x1b[0m, line \x1b[1;36m17\x1b[0m, in \x1b[33mbar\x1b[0m                                            \x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m14 \x1b[0m\x1b[38;2;102;217;239;48;2;39;40;34mdef\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m \x1b[0m\x1b[38;2;166;226;46;48;2;39;40;34mget_exception\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m(\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m)\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m \x1b[0m\x1b[38;2;249;38;114;48;2;39;40;34m-\x1b[0m\x1b[38;2;249;38;114;48;2;39;40;34m>\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34mTraceback\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m:\x1b[0m\x1b[48;2;39;40;34m                                              \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m15 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m    \x1b[0m\x1b[38;2;102;217;239;48;2;39;40;34mdef\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m \x1b[0m\x1b[38;2;166;226;46;48;2;39;40;34mbar\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m(\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34ma\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m)\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m:\x1b[0m\x1b[48;2;39;40;34m                                                                \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m16 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m        \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34mprint\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m(\x1b[0m\x1b[38;2;174;129;255;48;2;39;40;34m1\x1b[0m\x1b[38;2;249;38;114;48;2;39;40;34m/\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34ma\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m)\x1b[0m\x1b[48;2;39;40;34m                                                             \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[38;2;101;102;96;48;2;39;40;34m❱ \x1b[0m\x1b[1;38;2;227;227;221;48;2;39;40;34m17 \x1b[0m\x1b[48;2;39;40;34m                                                                               \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m18 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m    \x1b[0m\x1b[38;2;102;217;239;48;2;39;40;34mdef\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m \x1b[0m\x1b[38;2;166;226;46;48;2;39;40;34mfoo\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m(\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34ma\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m)\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m:\x1b[0m\x1b[48;2;39;40;34m                                                                \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m19 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m        \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34mbar\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m(\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34ma\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m)\x1b[0m\x1b[48;2;39;40;34m                                                                 \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m20 \x1b[0m\x1b[48;2;39;40;34m                                                                               \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m╰──────────────────────────────────────────────────────────────────────────────────────╯\x1b[0m\n\x1b[1;38;5;9mZeroDivisionError: \x1b[0mdivision by zero\n\n\x1b[3mDuring handling of the above exception, another exception occurred:\x1b[0m\n\n\x1b[1mTraceback\x1b[0m \x1b[2m(most recent call last):\x1b[0m\n\x1b[34m╭──────────────────────────────────────────────────────────────────────────────────────╮\x1b[0m\n\x1b[34m│\x1b[0m File \x1b[32m"test_traceback.py"\x1b[0m, line \x1b[1;36m26\x1b[0m, in \x1b[33mget_exception\x1b[0m                                  \x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m23 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m            \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34mfoo\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m(\x1b[0m\x1b[38;2;174;129;255;48;2;39;40;34m0\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m)\x1b[0m\x1b[48;2;39;40;34m                                                             \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m24 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m        \x1b[0m\x1b[38;2;102;217;239;48;2;39;40;34mexcept\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m:\x1b[0m\x1b[48;2;39;40;34m                                                                \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m25 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m            \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34mfoobarbaz\x1b[0m\x1b[48;2;39;40;34m                                                          \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[38;2;101;102;96;48;2;39;40;34m❱ \x1b[0m\x1b[1;38;2;227;227;221;48;2;39;40;34m26 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m    \x1b[0m\x1b[38;2;102;217;239;48;2;39;40;34mexcept\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m:\x1b[0m\x1b[48;2;39;40;34m                                                                    \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m27 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m        \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34mtb\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m \x1b[0m\x1b[38;2;249;38;114;48;2;39;40;34m=\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34mTraceback\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m(\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m)\x1b[0m\x1b[48;2;39;40;34m                                                       \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m28 \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m        \x1b[0m\x1b[38;2;102;217;239;48;2;39;40;34mreturn\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34mtb\x1b[0m\x1b[48;2;39;40;34m                                                              \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m│\x1b[0m  \x1b[1;38;2;227;227;221;48;2;39;40;34m  \x1b[0m\x1b[38;2;101;102;96;48;2;39;40;34m29 \x1b[0m\x1b[48;2;39;40;34m                                                                               \x1b[0m\x1b[34m│\x1b[0m\n\x1b[34m╰──────────────────────────────────────────────────────────────────────────────────────╯\x1b[0m\n\x1b[1;38;5;9mNameError: \x1b[0mname \x1b[32m\'foobarbaz\'\x1b[0m is not defined\n'
