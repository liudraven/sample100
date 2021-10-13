# -*- coding:UTF-8 -*-
# auther:drliu
# aim: socket
from socket import *

#st = socket.socket(socket.AF_UNIX, socket.DGRAM)
st = socket()
st.bind('10.229.31.122')
st.listen(5)
inf_loop:
    data = st.accept()
    comm_loop:
        data.recv()
st.close()

