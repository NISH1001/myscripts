#!/bin/bash

for i in `seq 0 2`; 
do
    echo -n "thermal zone $i : "
    output="$(cat /sys/class/thermal/thermal_zone$i/temp)"
    echo ${output}
done

