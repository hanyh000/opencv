"""from tensorflow.keras.models import load_model

model = load_model("keras_Model.h5", compile=False)
print("모델 로딩 성공!")
"""
"""
import platform
print(platform.architecture()) 
"""
import os
import ctypes

dll_path = r"C:\Users\202-15\Desktop\py_opencv"
os.environ['PATH'] = dll_path + ";" + os.environ['PATH']

ctypes.cdll.LoadLibrary(os.path.join(dll_path, "libiconv.dll"))
ctypes.cdll.LoadLibrary(os.path.join(dll_path, "libzbar-64.dll"))