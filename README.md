# udp_frame_decoder


Environment：
Linux 5.0.0-25-generic #26-Ubuntu SMP x86_64 x86_64 x86_64 GNU/Linux
gcc (Ubuntu 8.3.0-6ubuntu1) 8.3.0
Python 3.7.3
libvpx v1.8.1 "Orpington Duck" 2019-07-15
Redis server v=5.0.3 sha=00000000:0 malloc=jemalloc-5.1.0 bits=64 build=23238c6957772153

Dependencies:
1. Compiling libvpx we need: 
    yasm doxygen curl sha1sum source ccache
    URL: https://chromium.googlesource.com/webm/libvpx/+archive/v1.8.1.tar.gz
2. Redis:
    redis-server redis-cli 
    sudo apt install redis libhiredis-dev python3-redis 
3. Python3:


Compilations:
1. libvpx:
    $ cd <your_path_to_libvpx>/libvpx
    $ mkdir mybuild
    $ cd  mybuild
    $ ../configure <configure options just like below>
    $ make
    
    my libvpx configure:
        --log=yes --target=x86_64-linux-gcc --enable-pic --enable-ccache \
        --enable-debug --enable-unit-tests --enable-decode-perf-tests --enable-encode-perf-tests \
        --enable-better-hw-compatibility --enable-vp8 --enable-vp9 --enable-internal-stats \
        --enable-postproc --enable-vp9-postproc --enable-error-concealment --enable-shared \
        --enable-multi-res-encoding --enable-vp9-temporal-denoising --enable-webm-io --enable-libyuv

2. udp_frame_decoder:
    $ cd udp_frame_decoder
    $ make
