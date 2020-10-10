<?php
class Category extends CategoryCore
{

    public $sub_description;

    public function __construct($id_category = null, $id_lang = null, $id_shop = null){
        self::$definition['fields']['sub_description'] = array('type' => self::TYPE_HTML, 'lang' => true);
        parent::__construct($id_category, $id_lang, $id_shop);
    }

}