from flask import jsonify
import test_utils as tu
import asyncio
import aiohttp

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            return response.status, url
    except aiohttp.ClientError as e:
        return type(e).__name__, url

async def get_urls_ref(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Test project urls (asyncio/aiohttp)
def test_project_urls(request):
    data = request.json
    file_path = data.get('file_path')

    passed = 0
    num_tests = 0
    comment = []
    model_response = []

    # ============= Test first_with_given_key =============
    get_urls = tu.import_function_or_class_from_file(file_path, tu.Function.GET_URLS)

    if get_urls[1] != 200:
        comment.append(f"Function {tu.Function.GET_URLS} not found")
    else:
        num_tests += 1
        urls = ['https://www.fit.vutbr.cz', 'https://www.szn.cz', 'https://office.com', 'https://www.alza.cz/']
        expected_output = asyncio.run(get_urls_ref(urls))
        print(expected_output)
        try:
            with tu.RestrictedEnvironment():
                result = asyncio.run(get_urls[0](urls))
                print(result)
                if result == expected_output:
                    passed += 1
                else:
                    #comment.append(f"Test case failed: {input_data}.\nExpected {expected_output}, but got {all_items}.")
                    comment.append(f"Test case failed: {urls}.\nExpected {expected_output}.")
        except Exception as e:
            comment.append("Test failed")

    result = {
        "comment": comment,
        "num_tests": num_tests,
        "passed": passed,
        "model_response": model_response
    }

    return jsonify(result)