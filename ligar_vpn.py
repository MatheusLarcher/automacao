from subprocess import Popen
from pywinauto import Desktop

app = Popen("C:\Program Files\OpenVPN Connect\OpenVPNConnect.exe", shell = True)


dialog = Desktop(backend='uia').window(title='OpenVPN Connect', found_index=0)
dialog.wait('visible')

        
def conectar_vpn(nome_vpn):
    vpn_button = dialog.child_window(title_re=".*widmen.*:")
    vpn_button[1].invoke()
    
def desconectar_vpn(nome_vpn):
    # Navigate to the specific group control and invoke it
    disconnect_button = dialog.child_window(title="Disconnect profile vpn-widmen.ccmcloud.com.br [Widmen]", control_type="Group")
    disconnect_button.wait('visible', timeout=10)
    
    # Since the control supports InvokePattern, we can use invoke() method
    disconnect_button.invoke()
    
    
conectar_vpn('empresa')

import time 
time.sleep(10)
desconectar_vpn('empresa')

