# this is a basic solution using multiple inputs and variables

from typing import Sized


slithy_adj = input("Give an adjective")
gyre_noun = input("Give a noun")
gimble_noun = input("Give another noun")
mimzy_adj = input("Give another adjective")
borogoves_propernoun = input("Give a proper noun")

word_arr = [slithy_adj, gyre_noun, gimble_noun, mimzy_adj, borogoves_propernoun]
print(f"Twas brillig in the {slithy_adj} toves did {gyre_noun} and {gimble_noun} in the wabe; all {mimzy_adj} were the {borogoves_propernoun}, and the mome wraths out grabe." )
