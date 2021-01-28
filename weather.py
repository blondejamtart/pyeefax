import subprocess
import json

from genericprovider import GenericProvider

fog = '''
           
- _ - _ - _
 - _ - _ - 
- _ - _ - _
           
'''

heavyRain = '''
  .-.      
 (   ).    
(___(__)   
 ,',','    
,',','     
'''

lightRain = '''
  .-.     
 (   ). 
(___(__)
 ' ' '  
  ' ' ' 
'''

snow = '''
  .-.      
 (   ).    
(___(__)   
 * * *     
  * * *    
'''

thunderRain = '''
  .-.      
 (   ).    
(___(__)   
 ; /Z ;   
 ; 7/ ;   
'''

thunderDry = '''
  .-.      
 (   ).    
(___(__)   
   /Z    
   7/  
'''

lightCloud = '''
        |/
  .-. -→@←-  
 (   )./|   
(___(__)                
'''

sun = '''
    | /    
   ,-,     
-→(   )←-  
   '-'     
  / |    
'''

heavyCloud = '''
           
    .--.   
 .-(    ). 
(___.__)__)
           
'''           

tableTop = ",------------,------------,------------,"

tableMid = "|------------+------------+------------|"

tableBot = "'------------'------------'------------'"


class WeatherProvider(GenericProvider):

    def __init__(self):
        super().__init__()
        self._dict_data = None

    def update(self):
        raw_json = subprocess.check_output(["./wego", "-frontend", "json"])
        raw_json = raw_json.decode('utf-8')
        
        self._dict_data = json.loads(raw_json[raw_json.find('{'):])
        self.data = ["", "", "", ""]

    def prettify(self, weather_state):
        pretty = {"head": "", "body": "", "foot": ""}
        s_time, s_date = weather_state["Time"].split('T')
        pretty["head"] = "  {0}\n   {1}".format(s_date, s_time)
        

    
