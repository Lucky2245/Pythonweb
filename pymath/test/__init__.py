from mypthonlib import functions
def test_haversine():
  assert functions.haversine(52.3703, 4.288, 1.394, 39439.393) ==99483.39948
