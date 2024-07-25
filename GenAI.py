import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
from HTSApp.services import WebScrapping
import json
import re







def extract_json(str_json):
    try:
        # Try to find JSON object using regex
        match = re.search(r'(\{.*?\})', str_json, re.DOTALL)
        if match:
            # Extract the JSON string
            json_str = match.group(1)
            # Correct common formatting issues if necessary (e.g., replacing single quotes with double quotes)
            json_str = json_str.replace("'", '"')
            # Parse the JSON data
            data = json.loads(json_str)
            return data
        else:
            raise ValueError("No JSON object found")
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        # If initial parsing fails, attempt a more robust recovery or notify the error
        return None


def web_scrapper(url):
  text_content = WebScrapping.fetch_website_text(url)
  return text_content




def generate_json(text_content, url):

  text1 = f"""Given the following web page content: "{text_content}", extract detailed information in a structured JSON format. The required details include:
- Company name: The name of the ecommerce company from the URL: "{url}"
- Unique Identification Number 1, 2, and 3: Extract up to three unique identifiers for the product. If fewer than three identifiers are found, fill the remaining 2 fields with "null" only.
- Product Name: The name of the product as listed on the webpage.
- Country of Origin: The country where the product was manufactured.
- Size: The size specification of the product, if applicable.
- Weight: The weight of the product, if mentioned.
Keys name should be this: Company_Name, Unique_Identification_Number_1, Unique_Identification_Number_2, Unique_Identification_Number_3, Product_Name, Country_of_Origin, Size, Weight

Format the output as JSON key-value pairs. If any value in the JSON has a double quote, make sure it is escaped with a backslash.
"""


  
  text1 = f"""Given the following web page content: "{text_content}", extract detailed information in a structured JSON format. The required details include:
- Company name: The name of the ecommerce company from url and use professional name : "{url}"
- Unique Identification Number 1, 2, and 3: Extract up to three unique identifiers for the product. If fewer than three identifiers are found, fill the remaining fields with "null" only.
- Product Name: The name of the product as listed on the webpage.
- Country of Origin: The country where the product was manufactured.
- Size: The size specification of the product, if applicable.
- Weight: The weight of the product, if mentioned.
Keys name should be this: "CompanyName", "UniqueIdentificationNumber1", "UniqueIdentificationNumber2", "UniqueIdentificationNumber3", "ProductName", "CountryOfOrigin", "Size", "Weight"
make sure if there is none or null at value side it should be inverted comma only


Format the output as JSON key-value pairs. Make sure every key and value in json are in double inverted comma, If any value in the JSON has a double quote, make sure it is escaped with a backslash."""






  #vertexai.init(project="jovial-meridian-428719-b1", location="us-central1")
  model = GenerativeModel(
    "gemini-1.5-pro-001",
  )
  responses = model.generate_content(
      [text1],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=True,
  )
  print("\n\n\n")

  str_json = "---->   "
  for response in responses:
    str_json  = str_json + " " + response.text

  str_json = str_json.replace("'", "")
  print(str_json)
  json_data = extract_json(str_json)
  print(json_data)


  #adding this 

  for key in json_data:
    if isinstance(json_data[key], str):  # Check if the value is a string
        json_data[key] = json_data[key].replace('"', '').replace("'", '')

  json_data = {key.replace(' ', ''): value for key, value in json_data.items()}


  json_data["ProductURL"] = url

  for key in json_data:
     json_data[key] = str(json_data[key])
     

  
  return (json_data)
  


def generate_desc(text_content):

  text_for_desc = f"""
  Create a product description that is strictly 105 characters or fewer, focusing only on the essential attributes such as material, use, and primary function for HTS code determination. Avoid explanations and special characters. The description must be directly relevant to the product's identity, concise, and adhere to the character limit, including spaces and any characters.

  Detailed Product Information: {text_content}

  Reminder: The output should be a clear, direct product description without any additional explanation. Ensure all characters, including spaces, count towards the 105-character limit. Avoid using any special characters.
  """






  #vertexai.init(project="jovial-meridian-428719-b1", location="us-central1")
  model = GenerativeModel(
    "gemini-1.5-pro-001",
  )
  responses = model.generate_content(
      [text_for_desc],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=True,
  )

  print("\n\n\n\n")
  str_desc = ""
  for response in responses:
    str_desc  = str_desc + " " + response.text

  if len(str_desc)<=105:
     return str_desc
  else:
     generate_desc(text_content)
     
  

#url = "https://www.amazon.com/Cravings-Chrissy-Teigen-Stainless-Included/dp/B0D2JLG46R?pd_rd_w=3N4R0&content-id=amzn1.sym.a0a34a17-d48e-482a-9742-bc324f908aee&pf_rd_p=a0a34a17-d48e-482a-9742-bc324f908aee&pf_rd_r=JHG27MTDWB45DYQT2J1S&pd_rd_wg=os96W&pd_rd_r=984efef7-8edc-45b8-a19a-e25a290d3bf7&pd_rd_i=B0D2JLG46R&ref_=NewHome_B0D2JLG46R"
#url = "https://www.braceability.com/products/plus-size-knee-sleeve"
#url = "https://www.bhphotovideo.com/c/product/1762582-REG/lenovo_82x70005us_15_6_ideapad_slim_3.html/fci/35801"
#url = "https://puritycoffee.com/products/balance-whole-bean-coffee?variant=43310053163177&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gclsrc=aw.ds&wickedsource=google&wickedid=CjwKCAjwqMO0BhA8EiwAFTLgICaSYcac_TabSSPjlvdF_V28PQAzVW-jncWjjeErIrocS4eVSsZLpBoCI7YQAvD_BwE&wickedid=&wcid=20717188953&wv=4&tw_source=google&tw_adid=&tw_campaign=20717188953&utm_term=&utm_campaign=MC+%7C+PMax+-+All+Products&utm_source=adwords&utm_medium=ppc&hsa_acc=6132656535&hsa_cam=20717188953&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=CjwKCAjwqMO0BhA8EiwAFTLgICaSYcac_TabSSPjlvdF_V28PQAzVW-jncWjjeErIrocS4eVSsZLpBoCI7YQAvD_BwE"

#url = "https://www.hanes.com/hanes-originals-ultimate-men-rsquo-s-boxer-briefs-pack-moisture-wicking-stretch-cotton-assorted-prints-and-solids-3-pack.html"



#text_for_desc = f""" JUST WRITE 105 CHARACTERS OR LESS THAN THAT WHATEVER IT TAKES - DO NOT USE SPECIAL CHARACTERS - Given the detailed product information provided below, craft a concise description that captures essential attributes necessary for customs classification. The description must not exceed 105 characters. Focus specifically on the material, primary use, and function, which are pivotal for accurately determining the HTS code. The description should be compact and directly relevant to the product's identity to facilitate precise customs classification.

#Detailed Product Information:
#{text_content}

#The generated description should adhere strictly to the 105-character limit while including all critical details needed for HTS classification. And space or other special character will consider as 1 character so please take care about all."""


vertexai.init(project="qwiklabs-gcp-04-091cbe4fed8b", location="us-central1")
generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}


def result_desc(url):
  content = web_scrapper(url)
  product_json_data = generate_json(content,url)

  product_gen_desc = generate_desc(content)

  print(product_json_data)
  print(product_gen_desc)
  return product_json_data, product_gen_desc


#Testing
#result_desc(url)