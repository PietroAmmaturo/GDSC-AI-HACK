import fitz
import requests
import json
from config import SYSTEM_PROMPT, OLLAMA_HOST, OLLAMA_PORT


def parse_pdf(filename: str) -> str:
    doc = fitz.open(filename)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def generate_course(parsed_text: str):
    # Calls OLLAMA to generate the course
    url = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}/api/generate"
    headers = { "Content-Type": "application/json" }
    data = {
        "model": "gemma:2b",
        "system": SYSTEM_PROMPT,
        "prompt": parsed_text,
        "format": "json",
        "stream": False
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        return actual_response
    else:
        raise Exception("Failed to generate course")
    


with open("output.json", encoding="UTF-8", mode="w") as f:
    f.write(generate_course("""
                China,[j] officially the People's Republic of China (PRC),[k] is a country in East Asia. With a population exceeding 1.4 billion, it is the world's second-most populous country. China spans the equivalent of five time zones and borders fourteen countries by land.[l] With an area of nearly 9.6 million square kilometers (3,700,000 sq mi), it is the third-largest country by total land area.[m] The country is divided into 33 province-level divisions,[n] inclusive of 22 provinces,[n] five autonomous regions, four municipalities, and two semi-autonomous special administrative regions. Beijing is the national capital, while Shanghai is its most populous city and largest financial center.

One of the cradles of civilization, China has been inhabited since the Paleolithic era, with the earliest dynasties emerging in the Yellow River basin before the late second millennium BCE. The eighth to third centuries BCE saw a breakdown in the authority of the Zhou dynasty, accompanied by the emergence of administrative and military techniques, literature, philosophy, and historiography. In 221 BCE, China was unified under an emperor for the first time. Appointed non-hereditary officials began ruling counties instead of the aristocracy, ushering in more than two millennia of imperial dynasties including the Qin, Han, Tang, Yuan, Ming, and Qing. With the invention of gunpowder and paper, the establishment of the Silk Road, and the building of the Great Wall, Chinese culture—including languages, traditions, architecture, philosophy and technology—flourished and has heavily influenced East Asia and beyond.

After decades of struggle, the monarchy was overthrown in 1912 and the Republic of China (ROC) was established. Despite China's eventual victory in the Second Sino-Japanese War and the Pacific War in general, numerous atrocities such as the Nanjing Massacre left lasting effects on the country. Concurrently during this period, the Chinese Communist Party (CCP) and the Kuomintang (KMT) government were fighting sporadically since 1927, with a brief truce as a united front when Japan began invading the country. The second phase of the civil war resumed not long after Japan was defeated, and by 1949, the CCP had established control on most of the territories of the country. As the KMT retreated to Taiwan, the country was split with both sides claiming to be the sole legitimate government of China. After the land reforms, later attempts to realize communism failed—the Great Leap Forward led to a massive famine of millions of citizens, while the Cultural Revolution caused a chaotic period of persecution and zealous Maoist populism. In 1971, the PRC replaced the ROC as China's representation in the United Nations (UN). Following the Sino-Soviet split, the Shanghai Communiqué in 1972 marked the beginning of normalized relations with the United States. Economic reforms that began in 1978 led by reformists within the CCP moved the country away from a socialist planned economy toward an increasingly capitalist market economy, spurring significant economic growth, although liberal and democratic political reforms stalled after the June Fourth Incident in 1989.

China is a unitary one-party socialist republic led by the CCP. It is a founding member of the UN and one of the five permanent members of the UN Security Council. It is a founding member of several multilateral and regional organizations such as the AIIB, the Silk Road Fund, the New Development Bank, and the RCEP. It is a member of the BRICS, the G20, APEC, the SCO, and the East Asia Summit. Making up around one-fifth of the world economy, the Chinese economy is the world's largest economy by GDP at purchasing power parity, the second-largest economy by nominal GDP, and the second-wealthiest country, albeit ranking poorly in measures of democracy, human rights and religious freedoms. The country has been one of the fastest-growing major economies and is the world's largest manufacturer and exporter, as well as the second-largest importer. China is a nuclear-weapon state with the world's largest standing army by military personnel and the second-largest defense budget. It is a great power and a regional power.
"""))