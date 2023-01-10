import psutil
from colorama import Fore
from datetime import datetime
import subprocess

battery = psutil.sensors_battery()

print(Fore.GREEN + '''
██████╗░██╗░░░██╗██████╗░███████╗  ░█████╗░░██████╗
██╔══██╗██║░░░██║██╔══██╗██╔════╝  ██╔══██╗██╔════╝
██║░░██║██║░░░██║██║░░██║█████╗░░  ██║░░██║╚█████╗░
██║░░██║██║░░░██║██║░░██║██╔══╝░░  ██║░░██║░╚═══██╗
██████╔╝╚██████╔╝██████╔╝███████╗  ╚█████╔╝██████╔╝
╚═════╝░░╚═════╝░╚═════╝░╚══════╝  ░╚════╝░╚═════╝░''')

print("Welcome to Dude OS")

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print("Current Time :", current_time)

print('''
[1] Open Chrome
[2] Open Visual Studio Code
[3] Open Laptop Details
[4] Open Terminal
[5] Open File Manager
[6] Help''')

user = input('> ')

url = "google.com"

chrome_path = 'cd /Applicationsopen Google\ Chrome.app'

def new_func():
    subprocess.run(["gnome-terminal", "--", "google-chrome"])

def one_func():
    subprocess.run(["gnome-terminal", "--", "code"])

def two_func():
    subprocess.run(["gnome-terminal", "--"])

def three_func():
    print('''[1] Open Chrome
[2] Open Visual Studio Code
[3] Open Laptop Details
[4] Open Terminal
[5] Open File Manager
[6] Help''')

def four_func():
    print('''Architecture:            x86_64
  CPU op-mode(s):        32-bit, 64-bit
  Address sizes:         39 bits physical, 48 bits virtual
  Byte Order:            Little Endian
CPU(s):                  4
  On-line CPU(s) list:   0-3
Vendor ID:               GenuineIntel
  Model name:            Intel(R) Core(TM) i3-5010U CPU @ 2.10GHz
    CPU family:          6
    Model:               61
    Thread(s) per core:  2
    Core(s) per socket:  2
    Socket(s):           1
    Stepping:            4
    CPU max MHz:         2000.0000
    CPU min MHz:         500.0000
    BogoMIPS:            4190.29
    Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mc
                         a cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss 
                         ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arc
                         h_perfmon pebs bts rep_good nopl xtopology nonstop_tsc 
                         cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vm
                         x est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse
                         4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave av
                         x f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb
                          invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnm
                         i flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1
                          avx2 smep bmi2 erms invpcid rdseed adx smap intel_pt x
                         saveopt dtherm arat pln pts md_clear flush_l1d
Virtualization features: 
  Virtualization:        VT-x
Caches (sum of all):     
  L1d:                   64 KiB (2 instances)
  L1i:                   64 KiB (2 instances)
  L2:                    512 KiB (2 instances)
  L3:                    3 MiB (1 instance)
NUMA:                    
  NUMA node(s):          1
  NUMA node0 CPU(s):     0-3
Vulnerabilities:         
  Itlb multihit:         KVM: Mitigation: VMX disabled
  L1tf:                  Mitigation; PTE Inversion; VMX conditional cache flushe
                         s, SMT vulnerable
  Mds:                   Mitigation; Clear CPU buffers; SMT vulnerable
  Meltdown:              Mitigation; PTI
  Mmio stale data:       Unknown: No mitigations
  Retbleed:              Not affected
  Spec store bypass:     Mitigation; Speculative Store Bypass disabled via prctl
                          and seccomp
  Spectre v1:            Mitigation; usercopy/swapgs barriers and __user pointer
                          sanitization
  Spectre v2:            Mitigation; Retpolines, IBPB conditional, IBRS_FW, STIB
                         P conditional, RSB filling, PBRSB-eIBRS Not affected
  Srbds:                 Mitigation; Microcode
  Tsx async abort:       Not affected
''')

def five_func():
    subprocess.run(['xdg-open', '/home/navdeesh'])


while True:
    if user.isalpha or user.isalnum():
        if user.isnumeric():
            if int(user) == 1:
                new_func()
                user = input('> ')
            elif int(user) == 2:
                one_func()
                user = input('> ')
            elif int(user) == 4:
                two_func()
                user = input('> ')
            elif int(user) == 6:
                three_func()
                user = input('> ')
            elif int(user) == 3:
                four_func()
                user = input('> ')
            elif int(user) == 5:
                five_func()
                user = input('> ')
            else:
                print("I don't know this.")
                user = input('> ')
        else:
            print("I don't know this.")
            user = input('> ')
    elif int(user) == 1:
        new_func()
        user = input('> ')
    elif int(user) == 2:
        one_func()
        user = input('> ')
    elif int(user) == 4:
        two_func()
        user = input('> ')
    elif int(user) == 6:
        three_func()
        user = input('> ')
    elif int(user) == 3:
        four_func()
        user = input('> ')
    elif int(user) == 5:
        five_func()
        user = input('> ')
    else:
        print("I don't know this.")
        user = input('> ')
