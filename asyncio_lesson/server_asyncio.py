import asyncio

clients = []


async def handle_client(reader, writer):
    addr = writer.get_extra_info("peername")
    clients.append(writer)
    print(f"New connection from {addr}")

    try:
        while True:
            data = await reader.read(100)
            if not data:
                print(f"Connection from {addr} closed")
                break
            message = data.decode()
            print(f"Received {message} from {addr}")

            for client in clients:
                if client is not writer:
                    client.write(data)
                    await client.drain()
    except ConnectionResetError:
        print(f"Connection from {addr} lost")
    finally:
        clients.remove(writer)
        writer.close()
        await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 5001)
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")
    async with server:
        await server.serve_forever()


asyncio.run(main())
