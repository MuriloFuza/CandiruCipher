__author__ = "Murilo Fuza da Cunha"
__version__ = "1.0"
__email__ = "muriloacademix@gmail.com"
__status__ = "Prototype"

class CandiruCipher:
  def __init__(self) -> None:
    self.encryptingMessage = ''
    self.table = []
    self.encryptedMessage = ''
    self.keyGlobal = []
    self.keyFlow = 217
    self.messageRailFence = []
    self.messagePolyalphabetic = []
    self.messageFlow = []
    self.calc = 0
    self.table = [
      ['a', ' ','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b'],
      ['b','a', ' ','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c'],
      ['c','b','a', ' ','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d'],
      ['d','c','b','a', ' ','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e'],
      ['e','d','c','b','a', ' ','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f'],
      ['f','e','d','c','b','a', ' ','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g'],
      ['g','f','e','d','c','b','a', ' ','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h'],
      ['h','g','f','e','d','c','b','a', ' ','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i'],
      ['i','h','g','f','e','d','c','b','a', ' ','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j'],
      ['j','i','h','g','f','e','d','c','b','a', ' ','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k'],
      ['k','j','i','h','g','f','e','d','c','b','a', ' ','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l'],
      ['l','k','j','i','h','g','f','e','d','c','b','a', ' ','z','y','x','w','v','u','t','s','r','q','p','o','n','m'],
      ['m','l','k','j','i','h','g','f','e','d','c','b','a', ' ','z','y','x','w','v','u','t','s','r','q','p','o','n'],    
      ['n','m','l','k','j','i','h','g','f','e','d','c','b','a', ' ','z','y','x','w','v','u','t','s','r','q','p','o'],
      ['o','n','m','l','k','j','i','h','g','f','e','d','c','b','a', ' ','z','y','x','w','v','u','t','s','r','q','p'],
      ['p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a', ' ','z','y','x','w','v','u','t','s','r','q'],
      ['q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a', ' ','z','y','x','w','v','u','t','s','r'],
      ['r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a', ' ','z','y','x','w','v','u','t','s'],
      ['s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a', ' ','z','y','x','w','v','u','t'],
      ['t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a', ' ','z','y','x','w','v','u'],
      ['u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a', ' ','z','y','x','w','v'],
      ['v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a', ' ','z','y','x','w'],
      ['w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a', ' ','z','y','x'],
      ['x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a', ' ','z','y'],
      ['y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a', ' ','z'],
      ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a', ' '],
      [' ','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'],    
    ]
    self.positionLetter = { 
                           0: 'a',
                           1: 'b',
                           2: 'c',
                           3: 'd',
                           4: 'e',
                           5: 'f',
                           6: 'g',
                           7: 'h',
                           8: 'i',
                           9: 'j',
                           10 :'k',
                           11 :'l',
                           12 :'m',
                           13 :'n',
                           14 :'o',
                           15 :'p',
                           16 :'q',
                           17 :'r',
                           18 :'s',
                           19 :'t',
                           20 :'u',
                           21 :'v',
                           22 :'w',
                           23 :'x',
                           24 :'y',
                           25 :'z',
                           26 :' '
                           }
    
  def railFenceCipher(self):
    self.calc = len(self.encryptingMessage) / len(self.keyGlobal)
    
    if(len(self.encryptingMessage) % len(self.keyGlobal) > 0):
      self.calc =int(self.calc) + 1

    self.calc = int(self.calc)
    
    limit = len(self.encryptingMessage) - 1
    j = 0
    
    # quebrar em vetores
    for i in range(self.calc):
      temp = []
      for k in range(len(self.keyGlobal)):
        if(j <= limit):
          temp.append(self.encryptingMessage[j])
          j += 1
      self.messageRailFence.append(temp)
      
    
    if(len(self.messageRailFence[-1]) < len(self.keyGlobal)):
      calc = len(self.keyGlobal) - len(self.messageRailFence[-1]) 
      for i in range(calc):
        self.messageRailFence[-1].append('*')
                
    # colocar na ordem encriptada
    guard = 0
    for i in range(len(self.messageRailFence)):
      temp = [' ']*len(self.messageRailFence[i])
      for k in range((len(self.messageRailFence[i]))):
        if(guard <= limit):
          key = self.keyGlobal[k]
          letter = self.messageRailFence[i][k]     
          
          # verificando quantas voltas é necessario
          if(key > len(temp)):
            guard = 0
            while(guard == 0):
              if(key > len(temp)):
                key = int(key / len(temp))
              else:
                guard = 1
               
          temp[key - 1] = letter
        guard += 1 
      self.messageRailFence[i] = temp
      
    guard = 0
    while(guard != -1):      
      if(len(self.messageRailFence[guard]) < len(self.keyGlobal)):
        limit = len(self.keyGlobal) - len(self.messageRailFence[guard])
        for i in range(limit):
           if(len(self.messageRailFence[guard]) < len(self.keyGlobal)):
             self.messageRailFence[guard].append("*")
        guard += 1
      else:
        guard += 1
      
      if(guard == len(self.messageRailFence)):
        guard = -1
                                           
    # concatenar o resultado final
    aux = ''
    count = len(self.messageRailFence[0])
    for l in self.messageRailFence[1:]:
      assert len(l) == count
    n = len(self.messageRailFence)
    final_len = n * count
    aux = [self.messageRailFence[i % n][int(i / n)] for i in range(final_len)]
    aux = "".join(aux)
    aux = aux.replace('*',"")
      
    self.messageRailFence = aux
    print("RailFence: ", self.messageRailFence)
    
  def polyalphabeticCipher(self):
  
    aux = []
    aux = list(self.messageRailFence)
    limit = len(aux)
    guard = 0
    
    while(guard < limit):
      for i in range(len(self.keyGlobal)):
        if(guard < limit):
          pos = list(self.positionLetter.keys())[list(self.positionLetter.values()).index(aux[guard])]
          calc = len(self.table[0]) - (self.keyGlobal[i] % len(self.table[0]) ) 
          self.messagePolyalphabetic.append(self.table[pos][calc]) 
          guard += 1
  
    self.messagePolyalphabetic = "".join(self.messagePolyalphabetic)
    print("Polyalphabetic: ", self.messagePolyalphabetic)
    
    
  def flowCipher(self):
    final = ''
    pos = 0
    
    for c in self.messagePolyalphabetic:
      result = (ord(c) ^ self.keyGlobal[pos]) ^ self.keyFlow
      pos += 1
      if(pos >= len(self.keyGlobal)):
        pos = 0
        
      final += chr(result)
    print(final)
  

  def encrypt(self, message, key):
    
    res = key.split(',')
    res = [int(numeric_string) for numeric_string in res]
    self.keyGlobal = res
    self.encryptingMessage = message
    
    self.railFenceCipher()
    self.polyalphabeticCipher()
    self.flowCipher()
  
  def decrypt(self, messageEncrypted):
    pass