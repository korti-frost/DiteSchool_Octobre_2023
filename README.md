# DiteSchool_Octobre_2023

## Exercice 1:
Prenez un projet que vous avez déjà réalisé ou avec lequel vous êtes familier. Réfléchissez à la manière dont le passage au cloud aurait pu améliorer ce projet.
Identifiez des domaines spécifiques où l'utilisation du cloud aurait pu apporter des avantages et/ou des inconvénients.

## Exercice 2:
Revenez au projet que vous avez envisagé lors de l'exercice précédent, où vous avez réfléchi à comment le cloud aurait pu améliorer votre projet. Maintenant, votre tâche consiste à explorer les services AWS que vous auriez pu utiliser pour réaliser ces améliorations. Sélectionnez un ou plusieurs services AWS pertinents pour les domaines que vous avez identifiés, puis expliquez en détail ce que fait chaque service, comment il serait utilisé dans le contexte de votre projet, et pourquoi vous avez choisi ce service spécifique pour cette amélioration.

## Exercice 3:
Découvrir et essayer les différentes façons d'interagir avec AWS
1) Connectez-vous à votre compte AWS via la Console de Gestion AWS. Explorez l'interface, parcourez les services AWS, et obtenez une idée générale de son fonctionnement. Ensuite, créez un compartiment S3 (Bucket) et ajoutez un objet à l'intérieur.
2) Installez et configurez l'AWS CLI sur votre ordinateur. Lisez le contenu du compartiment S3.
3) Écrivez un script simple en utilisant l'un des SDK AWS, par exemple en utilisant le SDK Python Boto3, pour supprimer un objet du compartiment Amazon S3.

### Solutions: 
1)Saisissez "S3" dans la barre de recherche, puis cliquez sur "Créer un compartiment". Attribuez-lui un nom unique et choisissez la région "Paris". Laissez les autres paramètres avec leurs valeurs par défaut. Ensuite, ajoutez un objet dans ce compartiment.
2) Téléchargez le programme d'installation MSI AWS CLI pour Windows (64 bits) à partir du lien suivant : https://awscli.amazonaws.com/AWSCLIV2.msi
Une fois le téléchargement terminé, exécutez le programme d'installation.
Pour vérifier si l'installation s'est bien déroulée, ouvrez le menu Démarrer de Windows, recherchez "cmd" pour ouvrir une fenêtre d'invite de commandes, puis saisissez la commande "aws --version".
Cliquez sur votre nom dans le menu, puis sélectionnez "Mes autorisations de sécurité" dans le menu déroulant. Créez ensuite une clé d'accès dans la section "Gestion des clés d'accès".
Remarque : Ne tenez pas compte de l'alerte qui peut s'afficher.
Ensuite, ouvrez le terminal (invite de commandes) et saisissez la commande "aws configure". Vous serez invité à fournir les informations de la clé d'accès que vous avez créée, y compris la clé d'accès, la clé secrète, la région par défaut et le format de sortie.
Pour afficher le contenu d'un compartiment S3 (Bucket), utilisez la commande "aws s3api list-object-versions --bucket (NOM DU BUCKET)".
Remarque : Assurez-vous de remplacer "(NOM DU BUCKET)" par le nom réel de votre compartiment S3.
3) Installez Boto3 (si vous l'avez fait en Python)
[Exemple de Code ici](https://github.com/korti-frost/DiteSchool_Octobre_2023/blob/main/Exercice-3.py)
