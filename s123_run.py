import os
import sys

# ၁။ လိုအပ်တဲ့ Library ရှိမရှိ အရင်စစ်မယ်
try:
    import requests
except ImportError:
    print("[*] Installing requests library...")
    os.system("pip install requests")
    import requests

# ၂။ .so ဖိုင်ကို Import လုပ်မယ်
try:
    import s123_32bit.so
except ImportError as e:
    print(f"\n[!] Error: .so ဖိုင်ကို Import လုပ်လို့မရပါ။")
    print(f"အကြောင်းရင်း: {e}")
    print("[*] ဖိုင်နာမည် 's123_32bit.so' ဖြစ်မဖြစ် ပြန်စစ်ပေးပါ။")
    sys.exit()

# ၃။ အစီအစဉ်ကို စတင်မယ်
if __name__ == "__main__":
    try:
        # ဒီနေရာမှာ .so ထဲက banner ကို အရင်ပြချင်ရင် show_banner() ကို ခေါ်ရပါမယ်
        # ဒါပေမဲ့ s7andar15.py ရဲ့ logic အရ check_approval() ထဲမှာ banner ပါပြီးသားမို့
        # check_approval() ကို အရင်ခေါ်ပေးရမှာဖြစ်ပါတယ်
        
        if s123.check_approval():
            s123.start_bypass()
            
    except AttributeError:
        # အကယ်၍ function နာမည် မှားနေခဲ့ရင် (ဥပမာ start_bypass မဟုတ်ခဲ့ရင်)
        print("[!] Error: .so ထဲမှာ လိုအပ်တဲ့ Function ကို ရှာမတွေ့ပါ။")
    except KeyboardInterrupt:
        print("\n[!] အစီအစဉ်ကို ရပ်ဆိုင်းလိုက်ပါပြီ။")
        sys.exit()
