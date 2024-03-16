echo 1500000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq
echo 1500000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq
#echo 600000 > /sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq
#echo 600000 > /sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq
#echo 600000 > /sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq
#echo 600000 > /sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq
#echo 600000 > /sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq
#echo 600000 > /sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq
#echo -1 > /proc/sys/kernel/sched_rt_runtime_us
echo "Reading raw data..."
sleep 1
insmod mfmkmod.ko
rmmod mfmkmod.ko
echo "done"
echo 600000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq
echo 1500000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq
#echo 600000 > /sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq
#echo 1500000 > /sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq
#echo 600000 > /sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq
#echo 1500000 > /sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq
#echo 600000 > /sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq
#echo 1500000 > /sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq
echo "Extracting mfm track data from raw voltage values..."
python extract_mfm.py
python combine.py
echo "done"
