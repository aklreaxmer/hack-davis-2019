import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///researchportal.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("alex","123123", 0)
session.add(user)

user = User("kevin","GS123", 1)
session.add(user)

#1
lab = Lab("Kevin Lee", "https://www.linkedin.com/in/kevinlee1998/", "Please accept me into your lab/summer internship", "Bioinformatics")
session.add(lab)
comment = Comment("Really great friend and peer", "Alex", None, 1)
session.add(comment)

#2
lab = Lab("Alex Kramer", "https://www.linkedin.com/in/alexander-kramer-b93244159/", "I don't want to be a code monkey", "Bioinformatics")
session.add(lab)
comment = Comment("One of the smartest, most capable programmers I know", "Kevin Lee", None, 2)
session.add(comment)

#3
lab = Lab("Ian Davidson", "http://web.cs.ucdavis.edu/~davidson/", "Welcome! I am a Professor in the computer science department working on AI, machine learning and data mining algorithm development. With domain expert collaborators I work on applications of my work to areas with societal impacts such as neuroscience, intelligent tutoring systems and social network.", "AI")
session.add(lab)
comment = Comment("He is my ECS 170 professor. Thank you for listening to feedback about posting the slides.", "Anonymous", None, 3)
session.add(comment)

#4
lab = Lab("Cho-Jui Hsieh", "http://web.cs.ucla.edu/~chohsieh/", "I am interested in developing new algorithms and optimization techniques for large-scale machine learning problems. Currently, I am working on developing new machine learning models as well as improving the model size, training speed, prediction speed, and robustness of popular (deep learning) models.", "AI")
session.add(lab)

#5None,
#6
lab = Lab("Josh Mccoy", "http://joshmccoy.com/", "Welcome! I am Joshua McCoy, a games scholar who specializes in technical research including interactive storytelling, virtual characters, new modes of game play, and related areas.", "AI")
session.add(lab)

#7
lab = Lab("Gerald Quon", "https://qlab.faculty.ucdavis.edu/", "The QUON-titative computational biology lab at UC Davis focuses on developing and applying methods from machine learning and statistics to unravel the genetic basis of complex traits and diseases such as Alzheimer’s and cancer. Some examples of our research include ways to integrate heterogeneous data (genetic, epigenetic, transcriptional) to model how transcriptional regulatory networks change over time and with disease progression, predict which combinations of drugs are optimal for targeting specific cell types and cancer types, and predict how variation in genetics and environmental exposures interact to change our risk of developing complex diseases.", "AI")
session.add(lab)

#8
lab = Lab("Ilias Tagkopoulos", "http://tagkopouloslab.ucdavis.edu/", "Big ideas on small organisms: using computing to address biological questions", "AI")
session.add(lab)

#9
lab = Lab("Zhou Yu", "http://zhouyu.cs.ucdavis.edu/", "I design algorithms for real-time intelligent interactive systems that coordinate with user actions that are beyond spoken languages, including non-verbal behaviors to achieve effective and natural communications. In particular, I optimize human-machine communication via studies of multimodal sensing and analysis, speech and natural language processing, machine learning and human-computer interaction.", "AI")
session.add(lab)

#10
lab = Lab("Matt Bishop", "http://nob.cs.ucdavis.edu/~bishop/", "I do research in computer security. Currently, my interests seem to focus on election processes, data sanitization, and the insider problem. I also like teaching.", "Computer Security")
session.add(lab)

#11
lab = Lab("Hao Chen", "http://web.cs.ucdavis.edu/~hchen/", "My research focuses on computer security. I am interested in a broad range of security problems, including machine learning security, software security, and mobile and wireless security. I am a member of the Computer Security Laboratory.", "Computer Security")
session.add(lab)

#12
lab = Lab("Prem Devanbu", "http://web.cs.ucdavis.edu/~devanbu/", "Whassup! I am on the Faculty of the Computer Science Department at the University of California at Davis. I work in the area of software engineering and social analytics, and co-direct the DECAL Lab with Vladimir Filkov   See my academic vitae  for a summary, and/or  my research statement for more details. I also have a statement on my expert witness, and consulting work", "Computer Security")
session.add(lab)

#13
lab = Lab("Prasant Mohapatra", "https://spirit.cs.ucdavis.edu/", "Our focus is mainly in the area of computer networks with specializations in Wireless Networks, Mobile Communications and Systems, Cybersecurity, Wireless Performance, Quality and Security, and Network Analytics.", "Computer Science")
session.add(lab)

#14
lab = Lab("Biswanath Mukherjee", "http://networks.cs.ucdavis.edu/~mukherje/", "The objectives of this research are to design, develop, and understand the properties of various architectures for the next generation of lightwave networks, which can be deployed over local, access, metropolitan, and wide areas. These networks exploit the capabilities of evolving lightwave technology, e.g., dense wavelength division multiplexing (WDM) and tunable optical transceivers. How existing fiber-based electronic networks can be upgraded to accommodate WDM (and hence a few orders of bandwidth increase) is being examined, e.g., Internet Protocol (IP) over WDM.", "Computer Security")
session.add(lab)

#15
lab = Lab("Phillip Rogaway", "http://web.cs.ucdavis.edu/~rogaway/", "These days, my technical work in cryptography is paired with corresponding concerns for social and ethical issues connected to technology, especially the problem of mass surveillance. I’ve been working on a small book on that topic.", "Computer Security")
session.add(lab)

#16
lab = Lab("Angie Ghelli", "https://acgelli.faculty.ucdavis.edu/", "The Gelli Lab studies the pathogenesis of human fungal pathogens with a particular focus on fungi that disseminate to the central nervous system (CNS). Among the pathogens we study is Cryptococcus neoformans – the leading cause of fungal meningoencephalitis. Our studies are aimed at resolving the molecular mechanisms mediating the interplay between fungi and the CNS.", "Pharmacology")
session.add(lab)

#17
lab = Lab("James A. Letts", "https://letts.faculty.ucdavis.edu/", "Welcome to the Letts Lab! We study the structure, function and mechanism of membrane proteins that catalyze electron transport reactions and characterize their diverse roles in critical bioenergetic processes and beyond.", "Molecular Biology")
session.add(lab)

#18
lab = Lab("Rachael Bay", "https://baylab.github.io/", "The Bay Lab studies interactions between human-induced changes in the environment and evolutionary processes. This includes how animals respond to changes in their environment that are caused by humans as well as how evolution might mitigate some of the negative impacts of human-induced change.", "Evolution and Ecology")
session.add(lab)

#19
lab = Lab("Jimm Trimmer", "https://trimmer.faculty.ucdavis.edu/", "We study ion channel signaling complexes that underlie neuronal activity in the mammalian brain and develop renewable affinity reagents to better understand and manipulate neuronal function.", "Biochemistry")
session.add(lab)

#20
lab = Lab("Nitzan Shabek", "http://shabek-lab.ucdavis.edu/", "How is a physical stimulus (such as light, gravity, hormones, and metabolites) perceived and integrated into a signal transduction pathway, and how are these cellular events regulated by the proteolytic machinery?  Our research integrates cutting edge approaches from the fields of biochemistry, structural biology, and molecular and cellular biology to decode these sensing machineries and signaling pathways in plants, fungi, and humans. Our ultimate goal is to decipher fundamental biological pathways from the atomic to organismal level, and develop innovative strategies for the benefit of agriculture, environment, and human health.", "Molecular Biology")
session.add(lab)

#21
lab = Lab("Alex Nord", "https://nordlab.faculty.ucdavis.edu/", "Our research explores gene regulatory circuits and chromatin dynamics in the brain, studying how these features contribute to brain development, evolution, and function. We apply a combination of genomics, mouse- and cell-based models, and human genetics. Our work is rooted in basic and translational science, with an ultimate goal of understanding the biological components of human diseases and disorders of the brain and improving clinical care of afflicted individuals. To that end, we perform both experimental work and computational analysis to reveal function of primary DNA sequence, epigenomic modifications, and chromatin structure.", "Molecular Biology")
session.add(lab)

#22
lab = Lab("Norm Matloff", "http://heather.cs.ucdavis.edu/matloff.html", "Dr. Norm Matloff is a professor of computer science at the University of California at Davis, and was formerly a professor of statistics at that university. He is a former database software developer in Silicon Valley, and has been a statistical consultant for firms such as the Kaiser Permanente Health Plan. He was born and raised in the Los Angeles area, and has a PhD in pure mathematics from UCLA, specializing in probability/functional analysis and statistics.", "Statistics")
session.add(lab)

#23
lab = Lab("Neil Hunter", "http://microbiology.ucdavis.edu/hunter/", "We study an essential DNA-repair mechanism called homologous recombination and how this process is modulated and regulated during meiosis to facilitate the pairing and segregation of homologous chromosomes. Errors in meiosis are a leading cause of pregnancy miscarriage and congenital disease.", "Microbiology")
session.add(lab)
comment = Comment("I am in his lab", "Kevin Lee", None, 23)
session.add(comment)

#24
lab = Lab("Michael Turelli", "https://biology.ucdavis.edu/people/michael-turelli", "Theoretical population and quantitative genetics, speciation, and population biology of Drosophila, especially cytoplasmic incompatibility.", "Evolution and Ecology")
session.add(lab)
comment = Comment("I had him for BIS 101 and he was one of my favorite professors", "Kevin Lee", None, 24)
session.add(comment)

#25
lab = Lab("Ian Korf", "http://korflab.ucdavis.edu/", "This is the website for Ian Korf's research group at the Genome Center, UC Davis. Since 2004 we have been developing bioinformatics solutions to help tackle problems - both large and small - in the fast-moving field of genomics. Much of the research in our lab builds on collaborations with others, both at UC Davis and also further afield.", "Bioinformatics")
session.add(lab)


#26
lab = Lab("John Albeck", "https://www.mcb.ucdavis.edu/faculty-labs/albeck/", "Real-time single-cell biology, Information flow in single cells, Dynamic heterogeneity and drug responses, Expanding the single-cell repertoire", "Biochemistry")
session.add(lab)

#27
lab = Lab("Dan Starr", "https://starr.faculty.ucdavis.edu/people/", "Our lab studies processes involved in the positioning of nuclei and other organelles to specific locations within a cell. We are using the nematode Caenorhabditis elegans as a model organism. We use genetic, biochemical, cellular, and molecular approaches to study this basic problem in cell biology and human disease.", "Cell Biology")
session.add(lab)
comment = Comment("Currently in his BIS 104 class, and it is really interesting", "Kevin Lee", None, 27)
session.add(comment)

#28
lab = Lab("Frederic Chedin", "https://chedinlab.faculty.ucdavis.edu/", "My laboratory is focused on understanding the formation, function, and resolution of R-loop structures, a class of non-B DNA structures formed upon the annealing of an RNA strand to one strand of the DNA duplex. Genome-wide mapping data from my laboratory established that R-loop structures are prevalent in mammalian genomes and suggests that they represent a novel type of cis-acting functional DNA element.", "Genetics")
session.add(lab)

#29
lab = Lab("Louise Berben", "http://chemgroups.ucdavis.edu/~berben/", "We are a research group in the Department of Chemistry at the University of California and we address problems surrounding the environment, the storage of renewable and conventional energy, and electron transfer in molecular materials.", "Analytical Chemistry")
session.add(lab)

#30
lab = Lab("William Casey", "http://chemgroups.ucdavis.edu/~casey/content/research.html", "Equilibrium constants for aqueous systems that exist deep in the earth's crust are of great importance for chemists and geochemists. There exists a number of theoretical methods to determine equilibrium constants but remain mostly untested above pressures of 0.5 GPa. Our group is interested in using NMR as an analytical technique to determine these equilibria for these aqueous systems.", "Analytical Chemistry")
session.add(lab)

#31
lab = Lab("Ting Guo", "http://nanofast.ucdavis.edu/", "Professor Ting Guo's research group at UC Davis focuses on studying the mechanisms and control of energy exchanges between nanomaterials and between nanomaterials and their environment. The forms of energy include chemical energy, visible photon energy, and especially x-ray photon energy.", "Analytical Chemistry")
session.add(lab)

#32
lab = Lab("Alan Balch", "http://chemgroups.ucdavis.edu/~balch/", "The Balch Lab group focuses on inorganic chemistry. This includes fullerene cages, polymorphs, and crystalization of unstable molecules.", "Bioinorganic Chemistry")
session.add(lab)

#33
lab = Lab("Sheila David", "https://davidlab.ucdavis.edu/", "The David Lab at UC Davis utilizes numerous tools of chemical biology to explore the complex mechanistic details of DNA repair enzymes. DNA repair proteins such as MutY and NEIL, among the targets of research of the David Lab, help catalyze necessary repair of oxidative DNA damage, and are critical to maintaining genomic integrity in organisms living in the oxygen-rich environment of Earth.", "Bioinorganic Chemistry")
session.add(lab)

#34
lab = Lab("David Goodin", "http://www.goodinlab.com/", "Our research is focused on understanding how metalloenzymes operate. We are also working to re-engineer these enzymes to develop novel catalysts that are capable of oxidizing specific substrates. Our experimental approach involves the integrated use of multidisciplinary techniques including molecular biology, protein engineering, x-ray crystallography, electron paramagnetic resonance, electrochemistry, calorimetry and kinetics.", "Bioinorganic Chemistry")
session.add(lab)

#35
lab = Lab("R. David Britt", "http://brittepr.ucdavis.edu/", "The Britt lab is investigating structure and function of biologically significant enzymes with redox-active transition metal centers, clusters or organic radicals in their active site. We have focused these efforts on enzymes important in bioenergy such as the oxygen-evolving photosystem II and the H2-forming [FeFe] hydrogenase as well as the diverse and growing family of radical SAM enzymes that employ an adenosyl radical to initiate a wide range of chemical transformations.", "Bioinorganic Chemistry")
session.add(lab)

#36
lab = Lab("Delmar Larsen", "https://larsenlab.ucdavis.edu/", "Our laboratory is located in the Chemistry department at UC Davis. Our research extends across many scientific disciplines including biophysics, physical chemistry, molecular biology and computational modeling, where the common thread among these different scientific areas of study is the investigation and characterization of rapid condensed phase dynamics.", "Biophysical Chemistry")
session.add(lab)

#37
lab = Lab("J. Clark Lagarius", "https://www.mcb.ucdavis.edu/faculty-labs/lagarias/", "Our research focuses on the extended phytochrome superfamily, bilin-based light sensors widespread in both eukaryotes and prokaryotes. Light-switches whose function depends on color and intensity of light, phytochromes and cyanobacteriochromes regulate photosynthesis-associated gene expression to optimize light energy conversion and to regulate growth, movement and reproduction to avoid suboptimal light conditions.", "Biophysical Chemistry")
session.add(lab)

#38
lab = Lab("Justin Siegel", "https://sites.google.com/site/ucdsiegellab/", "Our goal is to live up to the classic tagline \"Better Living Through Chemistry\",  which we achieve through computational enzyme engineering.  Enzymes are the primary means by which biology performs chemical transformations.  Naturally evolved enzymes have been optimized over long periods of time to address challenges biological systems face in nature.", "Biophysical Chemistry")
session.add(lab)

posting = Posting("Hey, I'm a postdoctoral researcher in the Davidson lab. We're looking for a few undergraduate students with interest in computer vision to help with an ongoing research project involving facial recognition.", "Nicholas Kramer",  None, 3)
session.add(posting)
posting = Posting("The laboratory of Jennifer Lee, PhD, is seeking an Undergraduate Research Assistant to work closely with a post-doctoral researcher and laboratory technician on research involving cell biology, genome engineering, and ocular surgery. Minimum commitment: 1 year, 10+ hrs/wk.  Please email resumes to fakeEmail@ucdavis.edu for consideration.", "Dr. Jennifer Lee", None, 7)
session.add(posting)

session.commit()
