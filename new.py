import asyncio

import aiomysql
import data

async def main():
    pool = await aiomysql.create_pool(host="127.0.0.1",
                                      port=3306, user=data.username,
                                      password=data.password,
                                      db="zoo_shop")

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM animal")
            print(await cur.fetchall())
        pool.close()
        await pool.wait_closed()


async def create_animal(name, year, price):
    try:
        pool = await aiomysql.create_pool(host="127.0.0.1",
                                          port=3306, user=data.username,
                                          password=data.password,
                                          db="zoo_shop")
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = "INSERT INTO animal (name, year, price) values(%s,%s,%s)"
                await cur.execute(sql, (name, year, price))

                await conn.commit()
                print(f"Animal {name} has been added to the database")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pool.close()
        await pool.wait_closed()


async def change_price(animal_name, new_price):
    try:
        pool = await aiomysql.create_pool(host="127.0.0.1",
                                          port=3306, user=data.username,
                                          password=data.password,
                                          db="zoo_shop")
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = "UPDATE animal SET price = %s WHERE name = %s"
                await cur.execute(sql, (new_price, animal_name))

                await conn.commit()
                print(f"Animal {animal_name} has been updated to {new_price}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pool.close()
        await pool.wait_closed()


async def search_animal_by_partial_name(partial_name):
    try:
        pool = await aiomysql.create_pool(host="127.0.0.1",
                                          port=3306, user=data.username,
                                          password=data.password,
                                          db="zoo_shop")
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = "SELECT * FROM animal WHERE name LIKE %s"
                await cur.execute(sql, ('%'+partial_name+'%',))

                result = await cur.fetchall()
                if result:
                    print(f"Animal {partial_name} in {result}")
                else:
                    print(f"Animal {partial_name}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pool.close()
        await pool.wait_closed()


async def create_animal_staff(title, price):
    try:
        pool = await aiomysql.create_pool(host="127.0.0.1",
                                          port=3306, user=data.username,
                                          password=data.password,
                                          db="zoo_shop")
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = "INSERT INTO animal_staff (title, price) values(%s,%s)"
                await cur.execute(sql, (title, price))

                await conn.commit()
                print(f"Animal staff {title} has been added to the database")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pool.close()
        await pool.wait_closed()


if __name__ == "__main__":
    #asyncio.run(create_animal("Rex", 3, 7000))
    asyncio.run(change_price("mouse", 5000))
    asyncio.run(search_animal_by_partial_name("mo"))
    asyncio.run(create_animal_staff("pands", 250))
