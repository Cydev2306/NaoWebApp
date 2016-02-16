<?php

class Bootstrap extends Zend_Application_Bootstrap_Bootstrap
{
	public function run()
	{
		parent::run();
	}

	protected function _initDoctype() 
	{
		$this->bootstrap('view');
		$view = $this->getResource('view');
		$view->doctype('HTML5');
	}
	
	protected function _initEncoding() 
	{
		mb_internal_encoding("UTF-8");
	}
	
	protected function _initConfig()
	{
		Zend_Registry::set('configs', new Zend_Config($this->getOptions()));
	}
	
	protected function _initSession()
	{
		$session = new Zend_Session_Namespace('gestionProjet', true);
		return $session;
	}
	
	protected function _initDbAdapter()
	{
		$this->bootstrap('db');
		$db = $this->getResource('db');
		Zend_Db_Table::setDefaultAdapter($db);
	}
	protected function _initView()
	{
	    // Initialize view
	    $view = new Zend_View();
	    $view->doctype('XHTML1_STRICT');
	    $view->headMeta()->appendHttpEquiv('Content-Type',
	                                       'text/html; charset=utf-8');
	    $view->addHelperPath('Zend/Dojo/View/Helper/', 'Zend_Dojo_View_Helper');
	    $view->addHelperPath('App/View/Helper/', 'App_View_Helper');
	    $view->addHelperPath('ZendX/JQuery/View/Helper', 'ZendX_JQuery_View_Helper');
	    Zend_Dojo::enableView($view);
	    Zend_View_Helper_PaginationControl::setDefaultViewPartial('pagination.phtml');
	    // Add it to the ViewRenderer
	    $viewRenderer = Zend_Controller_Action_HelperBroker::getStaticHelper('ViewRenderer');
	    $viewRenderer->setView($view);
	    //seulement si on utilise d'autres frameworks ajax
	    ZendX_JQuery_View_Helper_JQuery::enableNoConflictMode();
	    // Return it, so that it can be stored by the bootstrap
	    return $view;
	}	
}
