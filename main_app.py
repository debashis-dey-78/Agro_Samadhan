# Library imports
import numpy as np
import streamlit as st
import cv2
from keras.models import load_model

# Loading the Model
model = load_model('plant_disease.h5', compile=False)

# Name of Classes
CLASS_NAMES = ['Broad_beans_Urahi-Cercospora_leaf_spot', 'Ridge_gourd_Zika-Alternaria_Leaf_Spot', 'Tomato-Leaf_Miner']

# Disease Information
disease_info = {
    'Broad_beans_Urahi-Cercospora_leaf_spot': """
        Disease Description :
        
        Cercospora leaf spot in beans can start either as a seed-borne illness, stunting and killing young plants as they emerge, or more commonly as a leaf spot that can spread to bean pods. Sun-exposed leaves often start to look sunburned, with reddish or purplish discoloration and a leathery appearance.

        Biology(Symptoms & Life Cycle):

        -A fungal disease which affects mostly older leaves.

        -The spots start as small brown flecks, expanding to brown round to slightly angular spots with grey centres up to 1 cm diameter (Photos 1-3). The spots have reddish-brown margins, sometimes with yellow halos. The spots dry and pieces fall out giving a ragged look. The fungus also causes spots on the pods and grows inside them.

        -Spread is by spores in wind and rain. Survival between crops is on seed, and in crop debris. It may also survive on weeds.

        Impact:
        
        A minor disease that is unlikely to affect yield. Usually, it occurs on the older dying leaves

        How to Detect?

        Look for the brown round to angular spots on the older leaves with greyish centres and darker margins, up to 1 cm diameter.

        Management:
        
        CULTURAL CONTROL

        Before planting:

        -Use wide spacing, 50 x 30 cm, so that air movement dries the leaves quickly after rains.
        -Avoid overlapping crops, preventing spores from older crops infecting newer ones. If not possible, then plant the newer crop far from those established already.

        During plant growth:

        -If practical, prune the older infected leaves when spots are first seen to prevent further spread of spores.
        Weed regularly.
        -In commercial plantings, use drip irrigation. If using overhead irrigation, time it so that plants dry out rapidly after watering. 

        After harvest:

        Collect and burn or plough in trash.
        Practice crop rotation, using maize or sorghum, or root crops, between crops of legumes planted on the same land.
        RESISTANT VARIETIES
        There are less susceptible varieties of cowpea and mung bean.

        CHEMICAL CONTROL:
        
        Treat seed with thiram, captan or mancozeb. It is very unlikely that fungicides will be required to control this disease in the field; if they are required, use mancozeb or copper.

    """,
    'Ridge_gourd_Zika-Alternaria_Leaf_Spot': """
        Description:

        -Alternaria is one of the most common diseases of broccoli, kale, and other Brassica crops.
        -It is sometimes referred to as black spot.
        -It affects leaves, and often results in head rot. It can be severely yield limiting. 
        -While this disease is not new, it has become worse in recent years.

        How to Detect?

        -Leaf symptoms include round, brown spots with concentric rings.
        -Spots often have a yellow halo, and can crack through the middle.
        -Spots often occur first on older leaves.
        -As the disease spreads, leaves can develop enough spots that they begin to meld together to create large necrotic areas on leaves.
        -Head rot symptoms can first appear as small brown spots on an otherwise healthy head.
        -Heads with rot symptoms deteriorate quickly.

        Biology(Symptoms & Life Cycle):

        -Alternaria leaf spot symptom starts as small circular leaf spots on older leaves on cantaloupe, cucumber and watermelon. The disease is not commonly seen on other cucurbits.
        -The leaf spots can be few to numerous that are spread throughout the leaves. The spots start as small yellow chlorotic lesions with a white or brown center.
        -The spots can enlarge and the center of the spots may show a radial crack or break out after some time. The margin of the lesion tends to have a brown discoloration which creates a distinguishable outline.

        - Alternaria is potentially caused by three pathogens: Fungal causal agent: Alternaria cucumerina (blight), Alternaria alternata f. sp. cucurbitae (spot).

        - Alternaria is a fungus. It produces spores, which can be spread via wind, water and equipment.
        This fungus can infect any plant in the Brassica and Cucurbits family, but tends to be most damaging in broccoli ,ridge gourd , cucumber and  cauliflower.

        -Alternaria can enter farms through infected seeds.
        Once present, Alternaria can persist in residues. In some cases, Alternaria fungi will develop resting spores that allow them to survive in the soil.

        -This disease spreads in warm temperatures (60-78 degrees F), and during periods of high humidity (90% RH).
        -Alternaria spp. can also cause fruit rot on cantaloupe. Characteristic symptom is water soaked sections of the fruit and black growth on the rind of the fruit.

        Managing Alternaria :
        
        Monitoring:
        
        -Alternaria can appear in early spring , especially if it is seedborne.
        -Check transplants for dark brown spots.
        -It often becomes widespread in the field in late summer as temperatures and humidity increase.
        -Scout often for initial symptoms, especially if high humidity is forecasted.
        Cultural Controls:
        -Buy seeds from companies that screen for Alternaria. Check with your local seed rep if this information is not readily available.
        -Screen transplants for symptoms before bringing them into the field.
        -Let three years pass before you plant Brassicas in the same location.
        -Avoid over-fertilizing; Alternaria symptoms can be worse in fields with too much nitrogen.
        -Avoid planting Brassica crops in fields with poor drainage, or fields that may receive runoff from fields where Brassicas were recently grown.
        -Avoid working in plants when they are wet from rain, irrigation, or dew.
        -Increase airflow by spacing plants adequately apart. Ideal broccoli spacing is 10–18 inches apart in rows 18–36 inches apart.
        -Clean and sanitize trays used for starting seeds each year, as well as any equipment used in fields with disease pressure.

        Here are some pesticides for Alternaria leaf spot: 

        Carbendazim 12% + Mancozeb 63% WP :
        
        A wettable powder that can control leaf spot and rust disease in groundnut and blast disease in paddy crops

        Carbendazim + Mancozeb :
        
        A combination that can be used to manage foliar diseases like Alternaria leaf spot

        Other pesticides for Alternaria leaf spot include: 
        
        KRILAXYL GOLD, CABRIO TOP, PRIAXOR, RADOSTAR, NATIVO, KATYAYANI PROPI, BUONOS, OPERA. 

        Some chemical fungicides that can control Alternaria leaf spot include: Dithane M-45, Antrocol, Captan, Difolaton, Blitox-50.

        CAUTION: Mention of a pesticide or use of a pesticide label is for educational purposes only. Always follow the pesticide label directions attached to the pesticide container you are using. Be sure that the plant you wish to treat is listed on the label of the pesticide you intend to use. And observe the number of days between pesticide application and when you can harvest your crop. Remember, the label is the law.


    """,
    'Tomato-Leaf_Miner': """
        Description : 
        
        If you have squiggly trails on the leaves of your plants or big blotches of no chlorophyll, you probably have leaf miners. These are the larvae of moths, sawflies, beetles, or flies. The larvae actually live in the leaf, between the outer skin layers. The leaf tissue protects them.

        Adult leaf miners are tiny moths, sawflies, beetles, or flies. Most people never notice them. Though there are many different leaf miner species, they all have small caterpillars (moths) or maggots (everything else).

        The color of the larvae varies from cream, yellowish-green, to green, depending on the species. The larvae are hard to see because they live between the top and bottom cells of the leaf.

        The larva feed by chewing or gouging the leaf’s chlorophyll into their mouth. Behind the larva, these gouges leave trails or blotches of opaque or brown tissue damage filled with frass (feces). Sometimes the tracks are squiggly, sometimes they are patches, and sometimes they are both.

        Life Cycle of Leaf Miners:
        
        Leaf miners overwinter as pupae in the leaf litter and garden debris. They hatch in early spring when the weather warms. After mating, the adult female gets busy laying eggs on the bottom of leaves, especially new leaves. Old leaves are tougher, and the larva has trouble eating them.

        The egg stage is just a few days in warm weather. The larvae hatch from the eggs, chew into the layer between the leaf’s top and bottom and start eating. Some leaf miners live their entire life cycle in one leaf. Others drop to the soil when finished growing and pupate. 

        Are leaf miners harmful?
        
        Yes, leaf miners are harmful. They affect the amount of chlorophyll in the leaf, which means it cannot photosynthesize as much energy for the plant. Badly infested leaves can drop off the plant entirely. If too many of the plant’s leaves drop off, it can affect plant growth.

        For professional growers, leaf miner damage means edible plants are not marketable anymore. And cannot be consumed.

        Management for leaf miners:

        Leaf miners can be difficult to get rid of because they live between the inside of the leaf. The leaf’s surface shields them from most pesticides. Using Integrated Pest Management (IPM) can be a suitable solution.

        There are three types of control methods in IPM. Cultural controls , Biological controls and Chemical controls .

        Cultural Controls:
        
        -Cultural controls are the preferred method to control leaf miners. They do not hurt the environment as much as chemical controls and are cheaper than buying biological or chemical controls.
        -Make sure your plants have enough water, as drought stress can really weaken a plant. By the same token, fertilize the plants as recommended to keep them well fed. Healthy plants can withstand more damage and bounce back faster than stressed plants.

        -Till the Ground:
        
        After you remove the last of your fall plants from your garden, till the ground well. This aerates the soil. In addition, tilling will bury and destroy the pupa stage and they will die. This breaks the lifecycle of leafminer and gives your plants a break.

        Biological Controls:
        
        Unless there has been widespread indiscriminate spraying in an area, leaf miners should have many natural enemies. If you are having problems with a lack of predators, many organic nursery supply stores stock leaf miner preditors, which you can release in your vegetable garden or flower bed. You will have to tolerate a low level of leafminers or the preditors will starve and won’t be there to help control the problem in the future.

        Chemical Control:
        
        Chemical control should always be the last resort. Many chemical controls kill beneficial insects such as bees and leaf miner preditors as well as leaf miners. If you must control the leaf miners chemically, use the least toxic option. Apply chemical controls in the evening, after bees and preditors have gone in for the night. You do not want to kill them.

        Spinosad : 
        
        Spinosad, sold as Monterey garden insect spray, is derived from soil microbes and does not kill bees or other non-target insects. It just kills the larva. As the leaf miner chews into the leaf, it consumes the spinosad and gets sick. It then stops feeding and eventually dies.

        Pyrethrin:
        
        This organic pesticide will kill leaf miners as they leave the egg and enter the leaf. Since they have to chew into the leaf, they ingest the poison with the leaf and die. However, pyrethrin also kills good insects such as bee and leaf miner preditors.

        What home remedy kills leaf miners?

        -Many people report successful control of leaf miners by spraying their plants with vegetable oil. The best way to use this is to pour two cups of vegetable oil into a spray container. Mix in two tablespoons of dishwashing liquid. Shake well and spritz on both sides of all the leaves until they have a light coating of oil on them.

        -This works because the oil covers the leaf miners and prevents oxygen from being absorbed from the skin into their bodies. The leaf miner larvae suffocate and die. This remedy takes time to work, so you may not see results for a few days.

    """
}

# Setting Title of App
st.title("AGRO-SAMADHAN(A Plant Disease Detection Tool)")
st.markdown("Upload an image of the plant leaf")

# Uploading the Plant image
plant_image = st.file_uploader("Choose an image...", type="jpg")
submit = st.button('Predict')

# On predict button click
if submit:
    if plant_image is not None:
        # Convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(plant_image.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        # Displaying the image
        st.image(opencv_image, channels="BGR")
        st.write(opencv_image.shape)

        # Resizing the image
        opencv_image = cv2.resize(opencv_image, (640, 640))

        # Convert image to 4 Dimension
        opencv_image.shape = (1, 640, 640, 3)

        # Make Prediction
        Y_pred = model.predict(opencv_image)
        result = CLASS_NAMES[np.argmax(Y_pred)]

        # Display disease information
        st.title(f"This is {result.split('-')[0]} leaf with {result.split('-')[1]}")
        st.markdown(disease_info[result])
