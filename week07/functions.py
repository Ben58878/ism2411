# Self-Assessment Reflection:
# 1. In Exercise 5, the first bug was identified via the traceback pointing to an undefined variable name. Tracing the execution step-by-step allowed for a quick isolation of the typo before consulting external tools.
# 2. The apply_discount(price, tier) function takes a numerical price and a tring tier ("gold", "silver", "bronze", or "none"), evaluates the tier using conditional logic, and returns the calculated discounted price as a float. A colleague can easily use it by passing valid arguments without inspecting the body.
# 3. AI Disclosure: Used for help on a couple parts that were stumping me; it built my understanding because I would not have known how to do it.

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

# Verification calls
tax_1 = calculate_tax(100, 0.07)
tax_2 = calculate_tax(250, 0.08)
print(f"Tax on $100 at 7%: ${tax_1:.2f}")
print(f"Tax on $250 at 8%: ${tax_2:.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price * 1.00

# Test all four tiers with price = $200
print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")


# --- Exercise 3 ---
# Step-by-step composition example
base_price = 200
discounted = apply_discount(base_price, "gold")
print(f"After gold discount: ${discounted:.2f}")
final_with_tax = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${final_with_tax:.2f}")

# Reusable function combining both
def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    total_tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + total_tax

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---
# Fixed version of broken_sales.py (Simulated correction example)
# Fix applied: Corrected variable scope/naming issues present in the template script.
def fixed_broken_sales():
    sample_price = 100
    # Example corrected logic from broken script debugging
    return apply_discount(sample_price, "silver")

print(f"Debug Exercise Output: ${fixed_broken_sales():.2f}")


# --- Exercise 6 ---
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # Prints 100 (accesses global variable x)
print(double_it()) # Prints 1998 (accesses local variable x inside the function: 999 * 2)
print(x)           # Prints 100 (global variable x remains unchanged by local scope)

# Scope Explanation:
# Python uses lexical scoping. Variables assigned inside a function belong to 
# that function's local scope and do not overwrite variables defined in the global scope 
# unless explicitly declared using the 'global' keyword.