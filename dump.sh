#!/bin/sh

#ATOP=/usr/bin/atop-1.27-3
ATOP=atop


if [ $# -eq 0 ]; then
	echo "Usage: " $0 " atop_raw_file"
	exit 0
fi

NAME=`basename $1`

TARGET=CPU
$ATOP -r $1 -P $TARGET | grep $TARGET | sed '1d' > $TARGET"_"$NAME.txt
TARGET=cpu
$ATOP -r $1 -P $TARGET | grep $TARGET | sed '1d' > $TARGET"_"$NAME.txt
TARGET=CPL
$ATOP -r $1 -P $TARGET | grep $TARGET | sed '1d' > $TARGET"_"$NAME.txt
TARGET=MEM
$ATOP -r $1 -P $TARGET | grep $TARGET | sed '1d' > $TARGET"_"$NAME.txt
TARGET=SWP
$ATOP -r $1 -P $TARGET | grep $TARGET | sed '1d' > $TARGET"_"$NAME.txt
TARGET=PAG
$ATOP -r $1 -P $TARGET | grep $TARGET | sed '1d' > $TARGET"_"$NAME.txt
TARGET=NET
$ATOP -r $1 -P $TARGET | grep $TARGET | sed '1d' > $TARGET"_"$NAME.txt
grep upper $TARGET"_"$NAME.txt | sed '1d' > upper_$TARGET"_"$NAME.txt
grep eth0 $TARGET"_"$NAME.txt | sed '1d' > eth0_$TARGET"_"$NAME.txt
grep eth3 $TARGET"_"$NAME.txt | sed '1d' > eth3_$TARGET"_"$NAME.txt
TARGET=DSK
$ATOP -r $1 -P $TARGET | grep $TARGET | sed '1d' > $TARGET"_"$NAME.txt


A="
CPU      Subsequent  fields:  
6 total  number of clock-ticks per second for this machine, 
7 number of processors, 
8 consumption for all
9 CPU's in system mode (clock-ticks), 
10 consumption for all CPU's in user mode (clock-ticks), 
11 consumption for all  CPU's  in user  mode  for niced processes (clock-ticks), 
12 consumption for all CPU's in idle mode (clock-ticks), 
13 consumption for all CPU's in wait mode (clock-ticks), 
14 consumption for all CPU's in irq mode (clock-ticks),  
15 consumption  for  all  CPU's  in softirq  mode  (clock-ticks),  
16 consumption  for  all CPU's in steal mode (clock-ticks), 
17 consumption for all CPU's in guest mode (clock-ticks).
"

CPU_DATA_FILE=CPU_$NAME.txt
CPU_PLOT_FILE=CPU_$NAME.png
gnuplot <<- EOF
set terminal png size 1200, 600
set lmargin 8
set rmargin 4
set tmargin 3
set bmargin 8
set timefmt "%H:%M:%S"
set format x "%H:%M:%S"
set xdata time
set output "${CPU_PLOT_FILE}"
set xtics rotate
set title "CPU"
plot "${CPU_DATA_FILE}" using 5:9 title "System mode" with lines, \
"${CPU_DATA_FILE}"using 5:10 title "User mode" with lines, \
"${CPU_DATA_FILE}"using 5:12 title "idle mode" with lines, \
"${CPU_DATA_FILE}"using 5:13 title "wait mode" with lines, \
"${CPU_DATA_FILE}"using 5:14 title "irq mode" with lines, \
"${CPU_DATA_FILE}"using 5:15 title "softirq mode" with lines, \
"${CPU_DATA_FILE}"using 5:16 title "steal mode" with lines, \
"${CPU_DATA_FILE}"using 5:17 title "guest mode" with lines
EOF


# Loading 

DATA_FILE=CPL_$NAME.txt
PLOT_FILE=Loading_$NAME.png
gnuplot <<- EOF
set terminal png size 1200, 600
set lmargin 8
set rmargin 4
set tmargin 3
set bmargin 8
set timefmt "%H:%M:%S"
set format x "%H:%M:%S"
set xdata time
set output "${PLOT_FILE}"
set xtics rotate
set title "CPU Loading"
plot "${DATA_FILE}" using 5:8 title "1 Min. Avg. loading" with lines, \
"${DATA_FILE}" using 5:9 title "5 Min. Avg. loading" with lines, \
"${DATA_FILE}" using 5:10 title "10 Min. Avg. loading" with lines
EOF


# CPL 

DATA_FILE=CPL_$NAME.txt
PLOT_FILE=CPL_$NAME.png
gnuplot <<- EOF
set terminal png size 1200, 600
set lmargin 8
set rmargin 4
set tmargin 3
set bmargin 8
set timefmt "%H:%M:%S"
set format x "%H:%M:%S"
set xdata time
set output "${PLOT_FILE}"
set xtics rotate
set title "CPU Loading information"
plot "${DATA_FILE}" using 5:11 title "Number of Context switching" with lines, \
"${DATA_FILE}" using 5:12 title "Number of serviced interrupts" with lines
EOF


# MEM

A="MEM      Subsequent  fields: 
7 page size for this machine (in bytes), 
8 size of physical memory (pages), 
9 size of free memory (pages),
10 size of page cache (pages), 
11 size of buffer cache (pages), 
12 size of slab (pages),
13 number of dirty pages in cache."


DATA_FILE=MEM_$NAME.txt
SWP_DATA_FILE=SWP_$NAME.txt
PLOT_FILE=MEM_$NAME.png
gnuplot <<- EOF
set terminal png size 1200, 600
set lmargin 8
set rmargin 4
set tmargin 3
set bmargin 8
set timefmt "%H:%M:%S"
set format x "%H:%M:%S"
set xdata time
set output "${PLOT_FILE}"
set xtics rotate
set title "Memory information"
plot "${DATA_FILE}" using 5:9 title "free memory" with lines, \
"${DATA_FILE}" using 5:10 title "page cache" with lines, \
"${DATA_FILE}" using 5:11 title "buffer cache" with lines, \
"${DATA_FILE}" using 5:12 title "slab" with lines, \
"${DATA_FILE}" using 5:13 title "dirty pages in cache" with lines, \
"${SWP_DATA_FILE}" using 5:11 title "SWAP: size of committed space" with lines, \
"${SWP_DATA_FILE}" using 5:12 title "SWAP: limit for committed space" with lines
EOF


# PAG

A="PAG      Subsequent  fields:  
page size for this machine (in bytes), 
8 number of page scans, 
9 number of allocstalls, 
10 0 (future use),
11 number of swapins,
12 number of swapouts."


DATA_FILE=PAG_$NAME.txt
PLOT_FILE=PAG_$NAME.png
gnuplot <<- EOF
set terminal png size 1200, 600
set lmargin 8
set rmargin 4
set tmargin 3
set bmargin 8
set timefmt "%H:%M:%S"
set format x "%H:%M:%S"
set xdata time
set output "${PLOT_FILE}"
set xtics rotate
set title "Paging"
plot "${DATA_FILE}" using 5:8 title "number of page scans" with lines, \
"${DATA_FILE}" using 5:9 title "number of allocs stalls" with lines, \
"${DATA_FILE}" using 5:11 title "number of swap ins" with lines, \
"${DATA_FILE}" using 5:12 title "Number of swap outs" with lines
EOF

# NET

A="       NET      First one line is produced for the upper layers of the TCP/IP stack.
Subsequent  fields: 
7 the verb 'upper', 
8 number of packets received by TCP, 
9 number of packets transmitted by TCP, 
10 number of packets received by UDP, 
11 number of packets transmitted by UDP, 
12 number of packets  received  by  IP,  
13 number  of  packets transmitted by IP, 
14 number of packets delivered to higher layers by IP,
15 number of packets forwarded by IP.
"

DATA_FILE=upper_NET_$NAME.txt
PLOT_FILE=upper_NET_$NAME.png
gnuplot <<- EOF
set terminal png size 1200, 600
set lmargin 8
set rmargin 4
set tmargin 3
set bmargin 8
set timefmt "%H:%M:%S"
set format x "%H:%M:%S"
set xdata time
set output "${PLOT_FILE}"
set xtics rotate
set title "Upper networking status"
plot "${DATA_FILE}" using 5:8 title "packets received by TCP" with lines, \
"${DATA_FILE}" using 5:9 title "packets transmitted by TCP" with lines, \
"${DATA_FILE}" using 5:10 title "packets received by UDP" with lines, \
"${DATA_FILE}" using 5:11 title "packets transmitted by UDP" with lines, \
"${DATA_FILE}" using 5:12 title "packets received by IP" with lines, \
"${DATA_FILE}" using 5:13 title "packets transmitted by IP" with lines, \
"${DATA_FILE}" using 5:14 title "packets delivered to higher layer by IP" with lines, \
"${DATA_FILE}" using 5:15 title "packets forwarded by IP" with lines
EOF


A="
Next one line is shown for every interface.
Subsequent  fields:  
7 name of the interface,
8 number of packets received by the interface, 
9  number of bytes received by the interface, 
10 number of packets transmitted by the interface, 
11 number of  bytes  transmitted  by  the  interface,  
12 interface speed,
13 duplex mode (0=half, 1=full).
"
DATA_FILE=eth0_NET_$NAME.txt
PLOT_FILE=eth0_NET_$NAME.png
gnuplot <<- EOF
set terminal png size 1200, 600
set lmargin 8
set rmargin 4
set tmargin 3
set bmargin 8
set timefmt "%H:%M:%S"
set format x "%H:%M:%S"
set xdata time
set output "${PLOT_FILE}"
set xtics rotate
set title "eth0 "
plot "${DATA_FILE}" using 5:8 title "packets received" with lines, \
"${DATA_FILE}" using 5:9 title "bytes received" with lines, \
"${DATA_FILE}" using 5:10 title "packets transmitted" with lines, \
"${DATA_FILE}" using 5:11 title "bytes transmitted" with lines
EOF


# DSK

A="For every logical volume/multiple device/hard disk one line is shown.
Subsequent fields: 
7 name, 
8 number of milliseconds spent for I/O, 
9 number of reads issued, 
10 number of sectors transferred for reads, 
11 number of writes issued, and 
12 number of sectors transferred for write."

DATA_FILE=DSK_$NAME.txt
PLOT_FILE=DSK_$NAME.png
gnuplot  <<- EOF
set terminal png size 1200, 600
set lmargin 8
set rmargin 4
set tmargin 3
set bmargin 8
set timefmt "%H:%M:%S"
set format x "%H:%M:%S"
set xdata time
set output "${PLOT_FILE}"
set xtics rotate
set title "Disk"
plot "${DATA_FILE}" using 5:8 title "ms spent for I/O" with lines, \
"${DATA_FILE}" using 5:9 title "reads issued" with lines, \
"${DATA_FILE}" using 5:10 title "sectors transferred for reads" with lines, \
"${DATA_FILE}" using 5:10 title "writes issues" with lines, \
"${DATA_FILE}" using 5:11 title "sectors transferred for writes" with lines 
EOF



