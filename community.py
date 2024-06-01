class Community:
  """
  A class to represent members of a community anchored by neighbors
   
  Attributes
  ----------
  community : [][int]
      A matrix of integers the same size as the input matrix, with
      a value of 0 or 1 to indicate members
  neighbors : [][row,col]
      a list of the neighbor addresses (row,col) that anchor the community

  Methods
  -------
  __init__      
    Constructor
  get_count()
    Returns the number of members in the community.
  """
  
  def __init__(self, matrix, distance):
    """
    Constructor - initilize the community, find the neighbors, and mark the members
    
    Parameters
    -------
    matrix : [][int] 
      2-dimensional array of integers. 
      Numbers > 0 are neighbors that anchor the community
    distance
      the distance from neighbors that should be counted in the community
      
    """
    self.community = self.initilize_community(matrix)
    self.neighbors = self.find_neighbors(matrix)
    self.build_community(distance)

  def get_count(self):
    """
    Get the number of members in the community.
    """
    total = 0
    for row in self.community:
      total += sum(row)
    return total
  
  def initilize_community(self, matrix):
    """
    Initilize the community to an all zero's matrix of the same size as the input matrix
    """
    community = []
    for row in matrix: 
      community.append([0]*len(row))
    return community

  def find_neighbors(self, matrix):
    """
    Find all the neighbors (value > 0) and make a list of their addresses
    """
    neighbors = []
    for row in range(len(matrix)):
      for col in range(len(matrix[row])):
        if matrix[row][col] > 0:
          neighbors.append([row,col])
    return neighbors

  def build_community(self, distance):
    """
    Find all the points that should be members of the community
    """
    for neighbor in self.neighbors:
      row = neighbor[0]
      col = neighbor[1]
      self.flag(row,col)

      for n in range(0,distance):
        row-=1
        while row < neighbor[0]:
          row+=1; col+=1; self.flag(row,col)

        while col > neighbor[1]:
          row+=1; col-=1; self.flag(row,col)

        while row > neighbor[0]:
          row-=1; col-=1; self.flag(row,col)

        while col < neighbor[1]:
          row-=1; col+=1; self.flag(row,col)
    
  def flag(self, row, col):
    """
    A bounds-safe setter for a member
    """
    if row >= 0 and \
      row < len(self.community) and \
      col >= 0 and \
      col < len(self.community[row]):
        self.community[row][col] = 1