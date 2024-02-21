from pipeline_langchain.pypeline_langchain import full_pipline
from utils.html_utils import all_sub_url


def company_check(data, model_llm, model_embedding):
    new_name = []
    # for web_link in data['Website']:
    for index in range(data.shape[0]):
        web_link = data.iloc[index]['Website']
        company_name = data.iloc[index]['Company Name']

        if not "https" in web_link:
            web_link = "https://" + web_link
        web_links = all_sub_url(web_link)
        qa_chain = full_pipline("web", model_llm, model_embedding, url_web=web_links)

        # query = data["Company Name"][0] + " is the real name of company, if yes, return" + data["Company Name"][0] +"if no, return NO"
        # query = data["Company Name"][0] + " is the real name of company, return only yes or no"

        query = ("Hello, "
                 "I need to verify the accuracy of the following name on your website: " + company_name +
                 "Please respond with only the name"
                 + company_name + "if it is correct. If" + company_name + " is incorrect,"
                 "provide an appropriate alternative name. Thank you for your assistance, "
                 "and please ensure the response is only the name. "
                 "I repeat, the result MUST BE ONE WORD")

        if qa_chain:
            result = qa_chain({"query": query})
            new_name.append(result['result'])
        else:
            new_name.append(company_name + "(Impossible)")

    data['Company Name'] = new_name
    return data
