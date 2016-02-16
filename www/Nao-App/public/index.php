<?php


defined('APPLICATION_PATH') || define('APPLICATION_PATH',
		realpath(dirname(__FILE__) . '/../application'));

defined('LIBRARY_PATH') || define('LIBRARY_PATH',
		realpath(dirname(__FILE__) . '/../library'));

defined('APPLICATION_ENV') || define('APPLICATION_ENV',
		(getenv('APPLICATION_ENV') ? getenv('APPLICATION_ENV') : 'production'));


//on modifie l'include path de php
set_include_path(implode(PATH_SEPARATOR, array(realpath(LIBRARY_PATH), get_include_path())));
//on modifie l'include path de php
set_include_path(implode(PATH_SEPARATOR, array(realpath(APPLICATION_PATH), get_include_path())));

//on lance la session
require_once 'Zend/Session.php';
Zend_Session::start();

// on a besoin de zend app pour lancer l'application
require_once 'Zend/Application.php';

//on appel l'autoloader
//require_once 'Zend/Loader.php';
//Zend_Loader::registerAutoload();
//Zend_Loader_Autoloader::getInstance();
require_once 'Zend/Loader/Autoloader.php';
$autoloader = Zend_Loader_Autoloader::getInstance();
$autoloader->setFallbackAutoloader(true);

//on créee l'application, on lance le bootstrap et l'application
$application = new Zend_Application(APPLICATION_ENV, APPLICATION_PATH . '/configs/application.ini');

// on lance l'appli
$application->bootstrap()->run();
?>
