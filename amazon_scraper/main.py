from scraper import scrape_amazon, parse_url


if __name__ == '__main__':
    URL = '''
    https://www.amazon.in/MSI-GeForce-Ventus-128-bit-Graphic/dp/B0C7W8GZMJ?dib=eyJ2IjoiMSJ9.VsRvMn0rzqVTPaeM1cWo332WcObX2BiFBJ_C_RodmqFcMcWvyc-SvyMeDJqAcDXdAIELk5YEg2XHb-Nq5Onk4cr7xRoR8P2g1-FoApNvokAaiidEQA1oYyThUm7GDQJ39opzqgi95NebcFhg6uRH8g-kqjQZ7PUt1f8rRqZJ2Ses9ZTyDbzD_eQul6CTgfh1IyI_NgLCEmCGogj3ycI0dR776f1D_BHz2KNv0wd2Rpo.DcSOxvnmWNzuDziIr7U8z_BcjfML8fITJuiOKFTSuOw&dib_tag=se&keywords=graphic%2Bcards&qid=1735564436&sr=8-8&th=1
    '''
    parsed_url = parse_url(URL)
    print(parsed_url)

    # scrape_amazon(URL, parse=True)