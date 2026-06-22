

# ─────────────────────────────────────────────
# SECTION 1 — Arithmetic Operators
# +  -  *  /  %  **  //
# ─────────────────────────────────────────────

def rectangle_metrics(length: float, width: float) -> None:
    """Calculate and display area & perimeter of a rectangle."""

    # + and * for perimeter/area
    area        = length * width            # *  multiplication
    perimeter   = 2 * (length + width)     # +  addition

    # % for remainder demo (e.g. tiling: how many full 0.5-unit tiles fit?)
    tile_size   = 0.5
    full_tiles  = area // tile_size        # // floor division
    leftover    = area % tile_size         # %  modulo (remainder)

    # ** for diagonal length via Pythagoras (a² + b²)
    diagonal    = (length ** 2 + width ** 2) ** 0.5   # ** exponentiation

    # - for difference between sides
    side_diff   = length - width           # -  subtraction

    print("=" * 52)
    print("  SECTION 1 — Arithmetic Operators")
    print("=" * 52)
    print(f"  Rectangle  : {length} × {width}")
    print(f"  Area       : {length} * {width}          = {area}")
    print(f"  Perimeter  : 2 * ({length} + {width})   = {perimeter}")
    print(f"  Diagonal   : ({length}² + {width}²)^0.5 = {diagonal:.4f}")
    print(f"  Side diff  : {length} - {width}          = {side_diff}")
    print(f"  Tiles(0.5) : {area} // {tile_size}       = {full_tiles} full tiles")
    print(f"  Leftover   : {area} %  {tile_size}       = {leftover}")


# ─────────────────────────────────────────────
# SECTION 2 — Comparison Operators
# >  <  ==  !=  >=  <=
# ─────────────────────────────────────────────

def compare_numbers(a: float, b: float) -> None:
    """Compare two numbers using every comparison operator."""

    print("\n" + "=" * 52)
    print("  SECTION 2 — Comparison Operators")
    print("=" * 52)
    print(f"  a = {a},  b = {b}")
    print()

    # Each operator used explicitly and its result printed
    print(f"  a >  b  ({a} >  {b})  → {a > b}")
    print(f"  a <  b  ({a} <  {b})  → {a < b}")
    print(f"  a == b  ({a} == {b})  → {a == b}")
    print(f"  a != b  ({a} != {b})  → {a != b}")
    print(f"  a >= b  ({a} >= {b})  → {a >= b}")
    print(f"  a <= b  ({a} <= {b})  → {a <= b}")
    print()

    # Human-readable verdict
    if a > b:
        print(f"  ➤ {a} is LARGER  than {b}")
    elif a < b:
        print(f"  ➤ {a} is SMALLER than {b}")
    else:
        print(f"  ➤ {a} and {b} are EQUAL")


# ─────────────────────────────────────────────
# SECTION 3 — Logical Operators
# and  or  not
# ─────────────────────────────────────────────

def logical_checks(number: float, text: str) -> None:
    """
    Evaluate conditions with and / or / not.
    Checks whether a number is in range and whether
    a string matches basic patterns.
    """

    LOW, HIGH = 10, 50

    # --- 'and': BOTH conditions must be true
    in_range = number >= LOW and number <= HIGH

    # --- 'or': AT LEAST ONE condition must be true
    is_extreme = number < LOW or number > HIGH

    # --- 'not': inverts a boolean
    not_in_range = not in_range

    # String pattern checks with logical operators
    is_greeting   = text.startswith("Hello") or text.startswith("Hi")
    is_short_greet = text.startswith("Hello") and len(text) <= 10
    not_empty     = not (text == "" or text.isspace())

    print("\n" + "=" * 52)
    print("  SECTION 3 — Logical Operators")
    print("=" * 52)
    print(f"  number = {number},  range = [{LOW}, {HIGH}]")
    print(f"  text   = {repr(text)}")
    print()
    print(f"  [and]  {number} >= {LOW} and {number} <= {HIGH}  → in_range     = {in_range}")
    print(f"  [or]   {number} <  {LOW} or  {number} >  {HIGH}  → is_extreme   = {is_extreme}")
    print(f"  [not]  not in_range                     → not_in_range = {not_in_range}")
    print()
    print(f"  [or]   starts with 'Hello' or 'Hi'     → is_greeting      = {is_greeting}")
    print(f"  [and]  starts with 'Hello' and len<=10 → is_short_greet   = {is_short_greet}")
    print(f"  [not]  not (empty or whitespace-only)  → not_empty        = {not_empty}")


# ─────────────────────────────────────────────
# SECTION 4 — Assignment & Augmented Assignment
# =   +=  -=  *=  /=  %=  **=
# ─────────────────────────────────────────────

def augmented_assignment_demo() -> None:
    """
    Show plain assignment vs every augmented assignment operator,
    with a realistic running-total scenario.
    """

    print("\n" + "=" * 52)
    print("  SECTION 4 — Assignment & Augmented Assignment")
    print("=" * 52)

    # Plain assignment (=)
    score = 100
    print(f"\n  score  =  100          → score = {score}")

    # +=  add to current value
    score += 25
    print(f"  score += 25            → score = {score}   (bonus points)")

    # -=  subtract from current value
    score -= 10
    print(f"  score -= 10            → score = {score}  (penalty)")

    # *=  multiply current value
    score *= 2
    print(f"  score *= 2             → score = {score}  (double-up round)")

    # /=  divide (result is always float)
    score /= 4
    print(f"  score /= 4             → score = {score} (quartered)")

    # %=  keep only the remainder after division
    score %= 20
    print(f"  score %= 20            → score = {score}   (mod 20)")

    # **= raise to a power
    score **= 3
    print(f"  score **= 3            → score = {score}  (cubed)")

    print()
    print("  Augmented assignments are shorthand:")
    print("  x += n  is exactly the same as  x = x + n")
    print("  They also re-use the same variable binding,")
    print("  which matters for mutable objects (lists, etc.).")

    # Demonstrate with a list counter
    items = []
    count = 0
    for fruit in ["apple", "banana", "cherry"]:
        items.append(fruit)
        count += 1     # +=  keeps a running tally
    print(f"\n  After adding 3 fruits → count = {count}, items = {items}")


# ─────────────────────────────────────────────
# SECTION 5 — Identity & Membership Operators
# is   is not   in   not in
# ─────────────────────────────────────────────

def identity_and_membership_demo() -> None:
    """
    Demonstrate identity operators (is / is not) and
    membership operators (in / not in).
    """

    print("\n" + "=" * 52)
    print("  SECTION 5 — Identity & Membership Operators")
    print("=" * 52)

    # ── Identity: 'is' checks object identity, NOT value equality ──
    print("\n  — Identity Operators (is / is not) —")

    a = [1, 2, 3]
    b = a            # b points to the SAME list object
    c = [1, 2, 3]   # c is a NEW list with equal content

    print(f"  a = [1,2,3]   (id={id(a)})")
    print(f"  b = a         (id={id(b)})  ← same object")
    print(f"  c = [1,2,3]   (id={id(c)})  ← different object, equal value")
    print()
    print(f"  a is b      → {a is b}   (same object in memory)")
    print(f"  a is c      → {a is c}  (different objects)")
    print(f"  a is not c  → {a is not c}   (correctly identified as distinct)")
    print(f"  a == c      → {a == c}   (values ARE equal, but objects differ)")

    # None identity — canonical use of 'is'
    result = None
    print(f"\n  result = None")
    print(f"  result is None      → {result is None}   ← preferred None check")
    print(f"  result is not None  → {result is not None}")

    # Small-int caching (CPython implementation detail)
    x, y = 256, 256
    print(f"\n  x, y = 256, 256")
    print(f"  x is y  → {x is y}  (CPython caches small ints -5 … 256)")

    # ── Membership: 'in' checks containment ──
    print("\n  — Membership Operators (in / not in) —")

    fruits   = ["apple", "banana", "cherry", "date"]
    search   = "banana"
    missing  = "mango"

    print(f"\n  fruits = {fruits}")
    print(f"  '{search}'  in     fruits → {search in fruits}")
    print(f"  '{missing}' in     fruits → {missing in fruits}")
    print(f"  '{missing}' not in fruits → {missing not in fruits}")

    # Membership on a string
    sentence = "Python makes operators easy to understand"
    word1, word2 = "operators", "difficult"

    print(f"\n  sentence = {repr(sentence)}")
    print(f"  '{word1}'  in sentence → {word1 in sentence}")
    print(f"  '{word2}' in sentence  → {word2 in sentence}")
    print(f"  '{word2}' not in sentence → {word2 not in sentence}")

    # Membership on a dict (checks keys)
    config = {"debug": True, "version": 3, "theme": "dark"}
    print(f"\n  config = {config}")
    print(f"  'debug'   in config → {'debug' in config}   (key exists)")
    print(f"  'timeout' in config → {'timeout' in config}  (key missing)")


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":

    # Section 1 — Arithmetic
    rectangle_metrics(length=8.0, width=5.0)

    # Section 2 — Comparison  (three cases: greater, less, equal)
    compare_numbers(15, 9)
    compare_numbers(4, 7)
    compare_numbers(6, 6)

    # Section 3 — Logical
    logical_checks(number=35, text="Hello, world!")
    logical_checks(number=5,  text="Hi")

    # Section 4 — Assignment & Augmented Assignment
    augmented_assignment_demo()

    # Section 5 — Identity & Membership
    identity_and_membership_demo()

    print("\n" + "=" * 52)
    print("  All operator demonstrations complete.")
    print("=" * 52)