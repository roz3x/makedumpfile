

make clean 
# CFLAGS=-fsanitize=thread 
CFLAGS=-DSHIVANG make USELZO=on LINKTYPE=dynamic -j10
# sudo gdb ./makedumpfile

[ -f ./vmcore ] && rm -f ./vmcore 
sudo ./makedumpfile -d 31 /proc/kcore vmcore -l --num-threads 20 
