<?php
class Application_Form_Questionreponse extends Twitter_Bootstrap_Form_Vertical
{
	public function init()
	{
		$this->addElement('textarea', 'question', array(
				'placeholder'   => 'Votre question',
				'rows' => '3'
		));
		
		$question = $this->getElement('question');
		$question->setRequired(true);
		
		$this->addElement('textarea', 'reponse', array(
				'placeholder' => 'Votre réponse',
				'rows' => '3'
		));
		
		$reponse = $this->getElement('reponse');
		$reponse->setRequired(true);

		$this->addElement('submit', 'Enregistrer', array(
				'buttonType'    => 'success'
		));
	}
}