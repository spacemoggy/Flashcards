# improve my function, use asyncio
import asyncio

async def test(name: str = "world") -> str:
    """Returns a personalized greeting.
    
    Args:
        name (str, optional): Name to include in greeting. Defaults to "world".
        
    Returns:
        str: A greeting string in the format 'Hello, {name}!'
    """
    return f"Hello, {name}!"

async def test_with_delay(name: str = "world", delay: float = 1.0) -> str:
    """Returns a personalized greeting after a delay.
    
    Args:
        name (str, optional): Name to include in greeting. Defaults to "world".
        delay (float, optional): Delay in seconds. Defaults to 1.0.
        
    Returns:
        str: A greeting string in the format 'Hello, {name}!'
    """
    await asyncio.sleep(delay)
    return f"Hello, {name}!"

async def test_multiple_greetings(names: list[str]) -> list[str]:
    """Returns greetings for multiple names concurrently.
    
    Args:
        names (list[str]): List of names to greet.
        
    Returns:
        list[str]: List of greeting strings.
    """
    tasks = [test(name) for name in names]
    return await asyncio.gather(*tasks)

async def test_with_validation(name: str = "world") -> str:
    """Returns a personalized greeting with input validation.
    
    Args:
        name (str, optional): Name to include in greeting. Defaults to "world".
        
    Returns:
        str: A greeting string in the format 'Hello, {name}!'
        
    Raises:
        ValueError: If name is empty or contains only whitespace.
    """
    if not name.strip():
        raise ValueError("Name cannot be empty or whitespace")
    return f"Hello, {name}!"

async def main():
    # Basic test
    print(await test())
    
    # Test with delay
    print(await test_with_delay("Alice", 0.5))
    
    # Test multiple greetings concurrently
    names = ["Bob", "Charlie", "David"]
    greetings = await test_multiple_greetings(names)
    print(greetings)
    
    # Test input validation
    try:
        await test_with_validation("")
    except ValueError as e:
        print(f"Validation error: {e}")

if __name__ == "__main__":
    asyncio.run(main())