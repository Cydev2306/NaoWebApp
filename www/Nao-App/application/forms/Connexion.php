<?php
class Application_Form_Connexion extends Twitter_Bootstrap_Form_Vertical
{
	public function init()
	{
		$this->addElement('text', 'login', array(
				'placeholder'   => 'Login',
				'class'         => 'large'
		));
		
		$login = $this->getElement('login');
		$login->addValidator(new Zend_Validate_EmailAddress(array()));
		$login->setRequired(true);
		
		$this->addElement('password', 'motDePasse', array(
				'placeholder' => 'Password',
				'class'         => 'large'
		));
		
		$motDePasse = $this->getElement('motDePasse');
		$motDePasse->setRequired(true);

		$this->addElement('submit', 'Connexion', array(
				'type'          => 'submit',
				'buttonType'    => 'success'
		));
	}
}