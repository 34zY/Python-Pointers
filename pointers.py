# ===================================================
# Understanding pointers in python from C
# Author : 34zY
# Github : https://github.com/34zY
# Doc : https://docs.python.org/3/library/ctypes.html
# ===================================================
import ctypes

# ===============================
# Declaring variable & Data types
# See https://docs.python.org/3/library/ctypes.html#fundamental-data-types
# Example ; 
a = ctypes.c_int(333) # declaring a variable in C through python (int)
print("[*] Type of A : " + str(a)) # c_long
print("[*] Value of A : " + str(a.value)) # value
# ================================


# ===============================
# Pointers
# See https://docs.python.org/3/library/ctypes.html#pointers
# Example ;
ptr = ctypes.pointer(a) # ptr pointing to the A value
print("[*] Variable Type (LP Pointer) : " + str(type(ptr))) # pointer LP (pointer)
print("[*] Pointer Type pointing to A : " + str(ptr.contents)) # c_long
print("[*] Pointer Value : " + str(ptr.contents.value)) # value pointed
print("[*] Pointer Address : " + str(ctypes.addressof(ptr.contents))) # Get the address of the pointer

ptr.contents.value = 777 # changing the value of the pointer 
print("[*] Value of A changed dynamically with pointer : " + str(a.value))
ptr.contents.value = 1234 # changing the value of the pointer 
print("[*] Value of A changed dynamically with pointer : " + str(a.value))
ptr.contents.value = 159 # changing the value of the pointer 
print("[*] Value of A changed dynamically with pointer : " + str(a.value))
# ================================

# ================================
# Casting
# Adding a new pointer to point into an existing address
ptr_address = ctypes.addressof(ptr.contents) # Put the address of the location of the variable object NOT the pointer itself 
ptr_new = ctypes.cast(ptr_address, ctypes.POINTER(ctypes.c_int)) # Store the address and his object type
print("[*] Value of A in an other pointer : " + str(ptr_new.contents.value))