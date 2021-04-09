from piston import Piston
import asyncio
# if using on windows use:
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
loop = asyncio.get_event_loop()
piston = Piston()


code = """
a = input("enter penis length: ")
print('your penis length is', a)
"""


async def func():
    out = await piston.execute(language="python3", stdin='1', source=code)
    print(out)
    versions = await piston.versions()
    for v in versions:
        print(v)
    
    

loop.run_until_complete(func())
loop.close()