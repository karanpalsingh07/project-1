annual_premium = 100000
sum_assured = 10 * annual_premium

premium_frequency = "quarterly"

if premium_frequency.lower() == "yearly":
    modal_premium = annual_premium
elif premium_frequency.lower() == "half-yearly":
    modal_premium = annual_premium / 2
elif premium_frequency.lower() == "quarterly":
    modal_premium = annual_premium / 4
elif premium_frequency.lower() == "monthly":
    modal_premium = annual_premium / 12 
else:
    print("invalid frequency.yearly.")  
    modal_premium = None

if modal_premium is not None:
    print("Sum Assured:",sum_assured)
    print("Model Premium:", modal_premium)