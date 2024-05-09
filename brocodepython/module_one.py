# --------------------------------------------------------------------------
# if __name__ == '__main__'
# ---------------------------------------------------------------------------

# y tho?
# 1.  Module can be run as a standalone program
# 2. Module can be important and used by other modules

# Python interpreter sets "special variables", one 0f which is __name__
# Python will assign the __name__ variable a value of '__main__' if its the initial module being run

import module_two

print(module_two.__name__)
print(module_two.main())