from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from interface.interface import Ui_MainWindow
from modules import journey_points, encounter, navigation, camping, hexgenerator
from data import acess_water_and_food as acessWF
from pyperclip import copy
from time import sleep
import sys 


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Old Dragon Tool")
        standardText = "Escolha as opções e clique em gerar."
        
		#Toggle Menu Button
        self.btn_superior.clicked.connect(self.LeftMenu)
        
        #Toggle Pages
        self.btnVIajandoErmos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.btnEncontroCombate.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btnHexcrawl.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        
        #Page: Pontos de Jornada
        self.pjPushButton_gerar.clicked.connect(self.getJorneyResult)
        self.pjPushButton_limpar.clicked.connect(lambda: self.pjLabel_result.setText(standardText))
        self.pjPushButton_copiar.clicked.connect(lambda: copy(self.pjLabel_result.text()))
        
        #Page: Navegação e Acampamento
        self.naPushButton_gerar.clicked.connect(self.getNavigationResult)
        self.naPushButton_gerarAcampamento.clicked.connect(lambda: self.naLabel_result.setText(camping.verifica_acampamento()))
        self.naPushButton_limpar.clicked.connect(lambda: self.naLabel_result.setText(standardText))
        self.naPushButton_copiar.clicked.connect(lambda: copy(self.naLabel_result.text()))
        
        #Page: Agua e Alimentaçao
        self.aaPushButton_gerar.clicked.connect(self.getWaterFoodResult)
        self.aaPushButton_limpar.clicked.connect(lambda: self.aaLabel_result.setText(standardText))
        self.aaPushButton_copiar.clicked.connect(lambda: copy(self.aaLabel_result.text()))
        
        #Page: Encontro nos Ermos
        self.eePushButton_gerar.clicked.connect(self.getWilderEncounter)
        self.eePushButton_limpar.clicked.connect(lambda: self.eeLabel_result.setText(standardText))
        self.eePushButton_copiar.clicked.connect(lambda: copy(self.eeLabel_result.text()))
        
        #Page: Encontro por tabelas
        self.etCheckBox_gerar.clicked.connect(self.getTableEncounter)
        self.etCheckBox_limpar.clicked.connect(lambda: self.etLabel_result.setText(standardText))
        self.etCheckBox_copiar.clicked.connect(lambda: copy(self.etLabel_result.text()))

        #Page: Hexcrawl
        self.hcPushButton_gerar.clicked.connect(self.getNewHex)
        self.hcPushButton_limpar.clicked.connect(lambda: self.hcLabel_result.setText(standardText))
        self.hcPushButton_copiar.clicked.connect(lambda: copy(self.hcLabel_result.text()))
        
    def getJorneyResult(self):
        action = ""
        local = ""
        
        if self.pjRadioButton_viajar.isChecked():
            action = 'viajar'
        elif self.pjRadioButton_descansar.isChecked():
            action = 'descansar'
        elif self.pjRadioButton_marchar.isChecked():
            action = 'marchar'
        elif self.pjRadioButton_acampar.isChecked():
            action = 'acampar'
        elif self.pjRadioButton_explorar.isChecked():
            action = 'explorar'
        elif self.pjRadioButton_forragear.isChecked():
            action = 'forragear'
        elif self.pjRadioButton_pescar.isChecked():
            action = 'pescar'
        elif self.pjRadioButton_cacar.isChecked():
            action = 'caçar'
            
        if self.pjRadioButton_planicie.isChecked():
            local = 'planicie'
        elif self.pjRadioButton_geleira.isChecked():
            local = 'geleira'
        elif self.pjRadioButton_colina.isChecked():
            local = 'colina'
        elif self.pjRadioButton_pantano.isChecked():
            local = 'pantano'
        elif self.pjRadioButton_floresta.isChecked():
            local = 'floresta'
        elif self.pjRadioButton_montanha.isChecked():
            local = 'montanha'
        elif self.pjRadioButton_deserto.isChecked():
            local = 'deserto'
                
        self.pjLabel_result.setText(journey_points.get_action_result(local, action))
    
    def getNavigationResult(self):
        local = ''
        haveLight = self.naCheckBox_luz.isChecked()
        haveRain = self.naCheckBox_nevoeiro.isChecked()
        haveTravel = self.naCheckBox_viajando.isChecked()
        
        if self.naRadioButton_planicie.isChecked():
            local = 'planicie'
        elif self.naRadioButton_geleira.isChecked():
            local = 'geleira'
        elif self.naRadioButton_colina.isChecked():
            local = 'colina'
        elif self.naRadioButton_pantano.isChecked():
            local = 'pantano'
        elif self.naRadioButton_floresta.isChecked():
            local = 'floresta'
        elif self.naRadioButton_montanha.isChecked():
            local = 'montanha'
        elif self.naRadioButton_deserto.isChecked():
            local = 'deserto'
        
        self.naLabel_result.setText(navigation.get_navigation(local, haveRain, haveLight, haveTravel))
    
    def getWaterFoodResult(self):
        local = ''
        season = ''
        climate = ''
        rangerPoints = self.aaSpinBox_pontos.value()
        morePeople = self.aaCheckBox_pessoas.isChecked()
        
        if self.aaRadioButton_planicie.isChecked():
            local = 'planicie'
        elif self.aaRadioButton_geleira.isChecked():
            local = 'geleira'
        elif self.aaRadioButton_colina.isChecked():
            local = 'colina'
        elif self.aaRadioButton_pantano.isChecked():
            local = 'pantano'
        elif self.aaRadioButton_floresta.isChecked():
            local = 'floresta'
        elif self.aaRadioButton_montanha.isChecked():
            local = 'montanha'
        elif self.aaRadioButton_deserto.isChecked():
            local = 'deserto'
        elif self.aaRadioButton_oceano.isChecked():
            local = 'oceano'
        
        if self.aaRadioButton_primavera.isChecked():
            season = 'primavera'
        elif self.aaRadioButton_outono.isChecked():
            season = 'outono'
        elif self.aaRadioButton_inverno.isChecked():
            season = 'inverno'
        elif self.aaRadioButton_verao.isChecked():
            season = 'verao'
        
        if self.aaRadioButton_polar.isChecked():
            climate = 'polar'
        elif self.aaRadioButton_temperado.isChecked():
            climate = 'temperado'
        elif self.aaRadioButton_tropical.isChecked():
            climate = 'tropical'
        
        if self.aaRadioButton_agua.isChecked():
            self.aaLabel_result.setText(acessWF.get_water_result(local, season, climate, rangerPoints))
        elif self.aaRadioButton_foragear.isChecked():
            self.aaLabel_result.setText(acessWF.get_forage_result(local, season, climate, rangerPoints))
        elif self.aaRadioButton_cacar.isChecked():
            self.aaLabel_result.setText(acessWF.get_hunt_result(local, season, climate, rangerPoints, morePeople))
    
    def getWilderEncounter(self):
        local = ''
        difficulty = ''
        level = ''
        danger = ''
        
        if self.eeRadioButton_planicie.isChecked():
            local = 'planicie'
        elif self.eeRadioButton_geleira.isChecked():
            local = 'geleira'
        elif self.eeRadioButton_colina.isChecked():
            local = 'colina'
        elif self.eeRadioButton_pantano.isChecked():
            local = 'pantano'
        elif self.eeRadioButton_floresta.isChecked():
            local = 'floresta'
        elif self.eeRadioButton_montanha.isChecked():
            local = 'montanha'
        elif self.eeRadioButton_deserto.isChecked():
            local = 'deserto'
        
        if self.eeRadioButton_facil.isChecked():
            difficulty = 'easy'
        elif self.eeRadioButton_mediano.isChecked():
            difficulty = 'normal'
        elif self.eeRadioButton_desafiador.isChecked():
            difficulty = 'hard'
        
        if self.eeRadioButton_iniciante.isChecked():
            level = 'beginner'
        elif self.eeRadioButton_heroico.isChecked():
            level = 'heroic'
        elif self.eeRadioButton_avancado.isChecked():
            level = 'advanced'
            
        if self.eeRadioButton_normal.isChecked():
            danger = 'normal'
        elif self.eeRadioButton_perigoso.isChecked():
            danger = 'dangerous'
        elif self.eeRadioButton_extremo.isChecked():
            danger = 'extreme'

        self.eeLabel_result.setText(encounter.test_encounter(local, difficulty, level, danger))
        
    def getTableEncounter(self):
        local = ''
        difficulty = ''
        level = ''
        danger = ''
        haveAnimal = self.etCheckBox_animais.isChecked()
        
        if self.radioButton_80.isChecked():
            local = 'planicie'
        elif self.etRadioButton_geleira.isChecked():
            local = 'geleira'
        elif self.etRadioButton_colina.isChecked():
            local = 'colina'
        elif self.etRadioButton_pantano.isChecked():
            local = 'pantano'
        elif self.etRadioButton_floresta.isChecked():
            local = 'floresta'
        elif self.etRadioButton_montanha.isChecked():
            local = 'montanha'
        elif self.etRadioButton_deserto.isChecked():
            local = 'deserto'
        elif self.etRadioButton_subterraneo.isChecked():
            local = 'subterraneo'
        elif self.etRadioButton_qualquer.isChecked():
            local = 'qualquer'
        elif self.etRadioButton_extraplanar.isChecked():
            local = 'extraplanar'
        elif self.etRadioButton_humano.isChecked():
            local = 'humano'
        
        if self.etRadioButton_facil.isChecked():
            difficulty = 'easy'
        elif self.etRadioButton_mediano.isChecked():
            difficulty = 'normal'
        elif self.etRadioButton_desafiador.isChecked():
            difficulty = 'hard'
        
        if self.etRadioButton_iniciante.isChecked():
            level = 'beginner'
        elif self.etRadioButton_heroico.isChecked():
            level = 'heroic'
        elif self.etRadioButton_avancado.isChecked():
            level = 'advanced'

        if not haveAnimal:
            self.etLabel_result.setText(encounter.get_encounter(local, difficulty, level))
        else:
            if local == 'qualquer' or local == 'extraplanar' or local == 'humano':
                self.etLabel_result.setText('Ao Escolher "Animais" você deve escolher um Bioma!') 
            else:
                self.etLabel_result.setText(encounter.get_encounter(local, difficulty, level, haveAnimal)) 
    
    def getNewHex(self):
        
        local = ''
        climate = ''
        
        if self.hcRadioButton_planicie.isChecked():
            local = 'planicie'
        elif self.hcRadioButton_geleira.isChecked():
            local = 'geleira'
        elif self.hcRadioButton_colina.isChecked():
            local = 'colina'
        elif self.hcRadioButton_pantano.isChecked():
            local = 'pantano'
        elif self.hcRadioButton_floresta.isChecked():
            local = 'floresta'
        elif self.hcRadioButton_montanha.isChecked():
            local = 'montanha'
        elif self.hcRadioButton_deserto.isChecked():
            local = 'deserto'
        elif self.hcRadioButton_oceano.isChecked():
            local = 'oceano'
    
        if self.hcRadioButton_polar.isChecked():
            climate = 'polar'
        elif self.hcRadioButton_temperado.isChecked():
            climate = 'temperado'
        elif self.hcRadioButton_tropical.isChecked():
            climate = 'tropical'
        
        self.hcLabel_result.setText(hexgenerator.generateHex(local, climate))
            
    def LeftMenu(self):
        
        width = self.barra_lateral.width()
        
        if width == 0:
            newwidth = 200
        else:
            newwidth = 0
        
        self.animation = QtCore.QPropertyAnimation(self.barra_lateral, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newwidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
            
if __name__ == "__main__":
    
    #Criando a Interface
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    