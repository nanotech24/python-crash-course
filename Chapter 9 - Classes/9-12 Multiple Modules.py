# C9-12 p.180(V2) Multiple Modules

# Notice that the User module is imported in the admin module
from Admin import *


my_admin = Admin('Richard', 'Sharpe', 26, 182, 95)

my_admin.show_privileges()