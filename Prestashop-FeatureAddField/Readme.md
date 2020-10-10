Ceci est un dossier contenant l'essentiel pour pouvoir sur Prestashop v. 1.6.1.24 d'insérer un champ supplémentaire.

Il s'agit d'inclure un footer en bas (footerDescriptionCategorie)
Catalogue > Catégorie
Le description en supplément du bas de page

Procédure pour implémenter un champ :
1) Ajouter le champ à la base de données.
    Sélectionner la table ps_category_lang
    Ajouter un champ via la requête sql phpmyadmin suivante :
    ALTER TABLE `ps_category_lang` ADD `sub_description` TEXT NULL AFTER `description`;


2) Ajouter le champ à l’objet catégorie de Prestashop
    Mettre dans www/override/classes/Category.php la version modifiée de www/classes/Category.php 


3) Ajoutons notre champ au formulaire de modification d’une catégories
    Copiez le fichier www/controllers/admin/AdminCategoriesController.php dans www/override/controllers/admin/AdminCategoriesController.php en ne conservant que l'essentiel


4) Vider le cache
5) Utilisation du nouveau champ en front
www/themes/nom-du-theme/templates/catalog/listing/category.tpl :
Sur le template catégorie il est possible d’afficher la valeur de notre champ avec {$category->sub_description}.

