tasks = [
    Task(id=1, description='Wake up at 8 am', 
         start_time= 8 ,duration=30, dependencies=[], preference= 8), 
    Task(id=2, description='Have breakfast', 
         start_time= 'NA', duration=60, dependencies=[1], preference= 6), 
    Task(id=3, description='Walk to Sookmyung’s library', 
         start_time= 'NA' ,duration=30, dependencies=[1], preference= 10), 
    Task(id=4, description='Work on the class’s prework', 
         start_time= 'NA', duration=90, dependencies=[1], preference= 8), 
    Task(id=5, description='Visit Gyeongbokgung Palace', 
         start_time= 'NA', duration=30, dependencies=[2], preference= 6), 
    Task(id=6, description='Ride the bus to the palace’s location', 
         start_time= 'NA', duration=30, dependencies=[2], preference= 3), 
    Task(id=7, description='Explore Insadong street art', 
         start_time='NA', duration=60, dependencies=[2], preference=7),
    Task(id=8, description='Try a local tea ceremony', 
         start_time='NA', duration=90, dependencies=[3], preference=10),
    Task(id=9, description='Read a book at a cozy café', 
         start_time='NA', duration=30, dependencies=[3], preference=10),
    Task(id=10, description='Attend a K-pop dance class', 
         start_time= 13, duration=10, dependencies=[3], preference=10)
]