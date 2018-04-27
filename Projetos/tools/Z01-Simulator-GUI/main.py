# -*- coding: utf-8 -*-
# Eduardo Marossi & Rafael Corsi @ insper.edu.br
# Dez/2017
# Disciplina Elementos de Sistemas
import sys, os, tempfile
import argparse

if sys.version_info[0] < 3:
    print ("Precisa ser o Python 3")
    exit();

import asm_utils, file_utils
import config_dialog

<<<<<<< HEAD
from PyQt5            import QtWidgets, uic, QtCore
from PyQt5.QtWidgets  import QApplication, QDialog, QMainWindow, QHeaderView, QFileDialog, QActionGroup, QAbstractItemView, QMessageBox, QProgressDialog
from PyQt5.QtGui      import QStandardItemModel, QStandardItem
from PyQt5.QtCore     import QModelIndex, QThread, QObject, QTime
from main_window      import *
from simulator_task   import SimulatorTask
from assembler_task   import AssemblerTask
from lst_parser       import LSTParser

PATH_APP       = os.path.dirname(os.path.abspath(__file__))
=======
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QHeaderView, QFileDialog, QActionGroup, QMessageBox, QProgressDialog, QVBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QDesktopServices
from PyQt5.QtCore import QThread, QTime, QFileSystemWatcher
from main_window import *
from simulator_task import SimulatorTask
from assembler_task import AssemblerTask
from lst_parser import LSTParser

>>>>>>> upstream/master

class AppMainWindow(QMainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

    def resizeEvent(self, event):
        self.resized.emit()
        return QMainWindow.resizeEvent(self, event)

<<<<<<< HEAD
class AppMain(Ui_MainWindow):
    RAM_VIEW_INITIAL_SIZE   = 1000
    TEMP_MAX_RAM_USE        = 1024*1000
    STEP_TIMER_IN_MS        = 1000

    def __init__(self):
        Ui_MainWindow.__init__(self)
        self.window      = AppMainWindow()
=======

class AppMain(Ui_MainWindow):
    RAM_VIEW_INITIAL_SIZE = 10000
    TEMP_MAX_RAM_USE = 1024*1000
    STEP_TIMER_IN_MS = 1000

    def __init__(self):
        Ui_MainWindow.__init__(self)

        ## class Variables
        self.config_dialog = None
        self.rom_stream = None
        self.rom_path = None
        self.rom_type_sel = None
        self.rom_model = None
        self.rom_watcher = None
        self.ram_model = None
        self.data_changed = None
        self.lst_parser = None
        self.last_step = None
        self.editor_converting = False
        self.pixmap_ALU = None
        self.asm_thread = None
        self.sim_thread = None
        self.config_dialog_ui = None
        self.actionROMGroup = None
        self.actionRAMGroup = None
        self.actionREGGroup = None
        self.step_timer = None
        self.window = AppMainWindow()

        # Setup Dialog, Editor, Actions, Threads, Img Resizing
>>>>>>> upstream/master
        self.setup_dialog()
        self.setupUi(self.window)
        self.setup_editor()
        self.setup_actions()
        self.setup_threads()
<<<<<<< HEAD
        self.setup_alu_image()

    def setup_alu_image(self):
        self.pixmap_ALU = QtGui.QPixmap("theme/alu.png")

    def setup_editor(self):
        self.rom_loaded        = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
        self.rom_type_sel      = self.actionROMAssembly
        self.lst_parser        = None
=======

    def show_alu(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile("theme/alu.png"))

    def setup_editor(self):
        self.rom_stream = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
        self.rom_path = None
        self.rom_type_sel = self.actionROMAssembly
        self.lst_parser = None
        self.rom_watcher = QFileSystemWatcher()
        self.rom_watcher.fileChanged.connect(self.reload_rom)
>>>>>>> upstream/master
        self.editor_converting = False
        self.spinBox.setValue(100)
        self.on_new()

    def setup_threads(self):
<<<<<<< HEAD
        self.asm_thread     = QThread()
        self.sim_thread     = QThread()
=======
        self.asm_thread = QThread()
        self.sim_thread = QThread()
>>>>>>> upstream/master

    def setup_dialog(self):
        self.config_dialog = QDialog()
        self.config_dialog_ui = config_dialog.Ui_Dialog()
        self.config_dialog_ui.setupUi(self.config_dialog)
        self.config_dialog_ui.assemblerLineEdit.setText("../jar/Z01-Assembler.jar")
        self.config_dialog_ui.rtlLineEdit.setText("../Z01-Simulator-rtl-2/")

    def setup_clean_views(self, table, rows=100, caption="Dados", line_header=None):
        model = QStandardItemModel(rows, 1, self.window)
        model.setHorizontalHeaderItem(0, QStandardItem(caption))
        table.setModel(model)
        for k in range(0, table.horizontalHeader().count()):
            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for l in range(0, rows):
            if line_header is None:
                model.setHeaderData(l, QtCore.Qt.Vertical, l)
            else:
                model.setHeaderData(l, QtCore.Qt.Vertical, line_header(l))
        return model

    def setup_actions(self):
        self.step_timer = QtCore.QTimer()
        self.step_timer.timeout.connect(self.on_proximo)
<<<<<<< HEAD
      
        self.window.resized.connect(self.resize_event)
=======

>>>>>>> upstream/master
        self.actionNovo.triggered.connect(self.on_new)
        self.actionSalvar_ROM.triggered.connect(self.on_save)
        self.actionAbrir.triggered.connect(self.on_load)
        self.actionProximo.triggered.connect(self.on_proximo)
        self.actionExecutarFim.triggered.connect(self.on_executar_fim)
        self.actionParar.triggered.connect(self.on_parar)
        self.actionEraseRAM.triggered.connect(self.on_clear_ram)
        self.actionVoltarInicio.triggered.connect(self.on_voltar_inicio)
        self.spinBox.valueChanged.connect(self.on_voltar_inicio)
        self.actionROMAssembly.triggered.connect(self.on_rom_assembly)
        self.actionROMBinario.triggered.connect(self.on_rom_binary)
<<<<<<< HEAD
        self.actionROMHexadecimal.triggered.connect(self.on_rom_hex)
        self.actionRAMHexadecimal.triggered.connect(self.on_ram_hex)
        self.actionRAMBinario.triggered.connect(self.on_ram_binary)

        self.actionROMGroup = QActionGroup(self.window)
        self.actionROMGroup.addAction(self.actionROMAssembly)
        self.actionROMGroup.addAction(self.actionROMBinario)
        self.actionROMGroup.addAction(self.actionROMHexadecimal)
        self.actionROMAssembly.setChecked(True)

        self.actionRAMGroup = QActionGroup(self.window)
        self.actionRAMGroup.addAction(self.actionRAMBinario)
        self.actionRAMGroup.addAction(self.actionRAMHexadecimal)
        self.actionRAMBinario.setChecked(True)

        self.actionREGGroup = QActionGroup(self.window)
        self.actionREGGroup.addAction(self.actionREGBinario)
        self.actionREGGroup.addAction(self.actionREGHexadecimal)
        self.actionREGBinario.setChecked(True)

=======
        self.actionROMGroup = QActionGroup(self.window)
        self.actionROMGroup.addAction(self.actionROMAssembly)
        self.actionROMGroup.addAction(self.actionROMBinario)
        self.actionROMAssembly.setChecked(True)
        self.but_ALU.clicked.connect(self.show_alu)
>>>>>>> upstream/master
        self.config_dialog_ui.procurarButton.clicked.connect(self.on_search_assembler)
        self.config_dialog_ui.alterarButton.clicked.connect(self.config_dialog.close)
        self.actionConfiguracoes.triggered.connect(self.config_dialog.show)

    def change_rtl_dir(self, new_dir):
<<<<<<< HEAD
    	self.config_dialog_ui.rtlLineEdit.setText(new_dir)

    def on_rom_assembly(self):
        self.editor_converting = True
        self.copy_file_to_model(self.rom_loaded, self.romModel)
=======
        self.config_dialog_ui.rtlLineEdit.setText(new_dir)

    def on_rom_assembly(self):
        self.editor_converting = True
        file_utils.copy_file_to_model(self.rom_stream, self.rom_model)
>>>>>>> upstream/master
        self.rom_type_sel = self.actionROMAssembly
        self.editor_converting = False

    def on_rom_binary(self):
        self.editor_converting = True
        if self.rom_type_sel == self.actionROMAssembly:
<<<<<<< HEAD
            self.copy_model_to_file(self.romModel, self.rom_loaded)
            self.assemble(self.load_converted_asm_bin)
        elif self.rom_type_sel == self.actionROMHexadecimal:
            temp = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
            self.copy_model_to_file(self.romModel, temp)
            self.copy_file_to_model(temp, self.romModel, asm_utils.hex_str_to_bin)
            self.editor_converting = False

        self.rom_type_sel = self.actionROMBinario

    def on_rom_hex(self):
        self.editor_converting = True

        if self.rom_type_sel == self.actionROMAssembly:
            self.copy_model_to_file(self.romModel, self.rom_loaded)
            self.assemble(self.load_converted_asm_hex)
        elif self.rom_type_sel == self.actionROMBinario:
            temp = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
            self.copy_model_to_file(self.romModel, temp)
            self.copy_file_to_model(temp, self.romModel, asm_utils.bin_str_to_hex)
            self.editor_converting = False

        self.rom_type_sel = self.actionROMHexadecimal

    def on_ram_binary(self):
        ## HEX TO BIN
        temp = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
        self.copy_model_to_file(self.ramModel, temp, asm_utils.hex_str_to_bin)
        self.copy_file_to_model(temp, self.ramModel)

    def on_ram_hex(self):
        temp = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
        self.copy_model_to_file(self.ramModel, temp)
        self.copy_file_to_model(temp, self.ramModel, asm_utils.bin_str_to_hex)

    def on_clear_ram(self):
        self.ramModel = self.setup_clean_views(self.ramView, rows=self.RAM_VIEW_INITIAL_SIZE, caption="RAM", line_header=asm_utils.z01_ram_name)
        for i in range(0, self.RAM_VIEW_INITIAL_SIZE):
            self.ramModel.setItem(i, QStandardItem("0000000000000000"))

    def on_new(self):
        self.on_clear_ram()
        self.romModel = self.setup_clean_views(self.romView, caption="ROM")
        self.romModel.itemChanged.connect(self.valid_rom)
        self.actionROMAssembly.setEnabled(True)

        self.clear_simulation()
        self.actionRAMBinario.setChecked(True)

    def on_voltar_inicio(self):
        self.changed = True
=======
            file_utils.copy_model_to_file(self.rom_model, self.rom_stream)
            self.assemble(self.load_converted_asm_bin)

        self.rom_type_sel = self.actionROMBinario

    def on_ram_tooltip(self, item):
        text = item.text().strip()

        try:
            val = int(text, 2)
        except ValueError:
            return

        item.setToolTip("{0:d} dec - {1:x} hex".format(val, val))

    def on_clear_ram(self):
        self.ram_model = self.setup_clean_views(self.ramView, rows=self.RAM_VIEW_INITIAL_SIZE, caption="RAM", line_header=asm_utils.z01_ram_name)
        for i in range(0, self.RAM_VIEW_INITIAL_SIZE):
            item = QStandardItem("0000000000000000")
            self.on_ram_tooltip(item)
            self.ram_model.setItem(i, item)


    def on_new(self):
        self.rom_path = None
        self.on_clear_ram()
        self.rom_model = self.setup_clean_views(self.romView, caption="ROM")
        self.rom_model.itemChanged.connect(self.valid_rom)
        self.ram_model.itemChanged.connect(self.valid_ram)
        self.actionROMAssembly.setEnabled(True)

        self.clear_simulation()

    def on_voltar_inicio(self):
        self.data_changed = True
>>>>>>> upstream/master
        self.clear_simulation()

    def on_parar(self):
        self.step_timer.stop()

    def on_executar_fim(self):
        self.step_timer.start(self.STEP_TIMER_IN_MS)

    def show(self):
        self.window.show()

    def on_save(self):
<<<<<<< HEAD
        filename = QFileDialog.getSaveFileName(self.window, "Salve o arquivo", os.getcwd(), "Arquivos (*.hack *.nasm)")
        if len(filename) == 0 or len(filename[0]) == 0:
            return None

        if self.actionROMAssembly.isChecked():
            self.copy_model_to_file(self.romModel, self.rom_loaded)

        file_utils.stream_to_file(self.rom_loaded, filename[0])
=======
        filename = self.rom_path

        if self.rom_path is not None:
            self.rom_watcher.removePath(self.rom_path)

        if filename is None:
            filename = QFileDialog.getSaveFileName(self.window, "Salve o arquivo", os.getcwd(), "Arquivos (*.hack *.nasm)")
            if len(filename) == 0 or len(filename[0]) == 0:
                return None
            filename = filename[0]
            self.rom_path = filename

        if self.actionROMAssembly.isChecked():
            file_utils.copy_model_to_file(self.rom_model, self.rom_stream)

        file_utils.stream_to_file(self.rom_stream, filename)
        self.rom_watcher.addPath(self.rom_path)
>>>>>>> upstream/master

    def on_load(self):
        filename = QFileDialog.getOpenFileName(self.window, "Escolha arquivo", os.getcwd(), "Arquivos (*.asm *.hack *.nasm)")
        if len(filename) == 0 or len(filename[0]) == 0:
            return None

<<<<<<< HEAD
        self.on_new()
        self.file_loaded = filename[0]

        if filename[0].endswith(".asm") or filename[0].endswith(".nasm"):
            self.load_asm(filename[0], self.romModel)
        elif filename[0].endswith(".bin") or filename[0].endswith(".hack"):
            self.load_bin(filename[0], self.romModel)
=======
        if self.rom_path is not None:
            self.rom_watcher.removePath(self.rom_path)

        self.on_new()
        self.rom_path = filename[0]
        self.rom_watcher.addPath(self.rom_path)
        self.reload_rom()

    def reload_rom(self):
        return self.load_rom(self.rom_path)

    def load_rom(self, filename):
        if not os.path.exists(filename):
            return

        if filename.endswith(".asm") or filename.endswith(".nasm"):
            self.load_asm(filename, self.rom_model)
        elif filename.endswith(".bin") or filename.endswith(".hack"):
            self.load_bin(filename, self.rom_model)
>>>>>>> upstream/master

    def on_search_assembler(self):
        filename = QFileDialog.getOpenFileName(self.window, "Escolha arquivo", os.getcwd(), "Arquivo JAR (*.jar)")
        if len(filename) == 0 or len(filename[0]) == 0:
            return None

        self.config_dialog_ui.assemblerLineEdit.setText(filename[0])

<<<<<<< HEAD
    def convert_to_format_regs(self,value):
        if self.actionREGHexadecimal.isChecked():
            return hex(int(value,2))
        else:
            return value

    def convert_to_format_ram(self, value):
        if self.actionRAMHexadecimal.isChecked():
            return hex(int(value, 2))
        else:
            return value

    def on_proximo(self):
        if self.changed:
=======
    def on_proximo(self):
        if self.data_changed:
>>>>>>> upstream/master
            if self.lst_parser is not None:
                self.lst_parser.close()

            if self.actionROMAssembly.isChecked():
<<<<<<< HEAD
                self.copy_model_to_file(self.romModel, self.rom_loaded)
                self.assemble(self.assemble_end)
            else:
                tmp_rom = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
                if self.actionROMHexadecimal.isChecked():
                    self.copy_model_to_file(self.romModel, tmp_rom, asm_utils.hex_str_to_bin)
                else:
                    self.copy_model_to_file(self.romModel, tmp_rom)
                tmp_ram = self.get_updated_ram()
                self.simulate(tmp_rom, tmp_ram)

            return False
            
=======
                file_utils.copy_model_to_file(self.rom_model, self.rom_stream)
                self.assemble(self.assemble_end)
            else:
                tmp_rom = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
                file_utils.copy_model_to_file(self.rom_model, tmp_rom)
                tmp_ram = self.get_updated_ram()
                self.simulate(tmp_rom, tmp_ram)
            return False

>>>>>>> upstream/master
        step = self.lst_parser.advance()

        if "s_regAout" not in step:
            self.step_timer.stop()
            QMessageBox.warning(self.window, "Simulador", "Fim de simulação")
            return

<<<<<<< HEAD
        self.update_line_edit(self.lineEdit_A,    self.convert_to_format_regs(step["s_regAout"]))
        self.update_line_edit(self.lineEdit_S,    self.convert_to_format_regs(step["s_regSout"]))
        self.update_line_edit(self.lineEdit_D,    self.convert_to_format_regs(step["s_regDout"]))
        self.update_line_edit(self.lineEdit_inM,  self.convert_to_format_regs(step["inM"]))
        self.update_line_edit(self.lineEdit_outM, self.convert_to_format_regs(step["outM"]))

        if self.last_step is not None:
            addr = int(step["s_regAout"], 2)
            index = self.ramModel.index(addr, 0)
            last_pc_counter = int(self.last_step["pcout"], 2) - 1

            if int(step["writeM"]) == 0 and int(step["selM"]) == 1 and int(self.last_step["selM"]) == 0:
=======
        self.update_line_edit(self.lineEdit_A, step["s_regAout"])
        self.update_line_edit(self.lineEdit_S, step["s_regSout"])
        self.update_line_edit(self.lineEdit_D, step["s_regDout"])
        self.update_line_edit(self.lineEdit_inM, step["inM"])
        self.update_line_edit(self.lineEdit_outM, step["outM"])

        if self.last_step is not None:
            addr = int(step["s_regAout"], 2)
            index = self.ram_model.index(addr, 0)
            last_pc_counter = int(self.last_step["pcout"], 2) - 1

            if int(step["writeM"]) == 0 and int(step["s_muxALUI_A"]) == 1 and int(self.last_step["s_muxALUI_A"]) == 0:
>>>>>>> upstream/master
               self.ramView.setCurrentIndex(index)

            if int(step["writeM"]) == 1:
               self.ramView.setCurrentIndex(index)
<<<<<<< HEAD
               self.ramModel.itemFromIndex(index).setText(self.convert_to_format_ram(step["outM"]))
=======
               self.ram_model.itemFromIndex(index).setText(step["outM"])
>>>>>>> upstream/master
        else:
            last_pc_counter = -1

        ## update ROM line
        pc_counter = int(step["pcout"], 2) - 1

        if pc_counter < 0:
            pc_counter = 0

        if pc_counter != last_pc_counter + 1:
            print("JUMP - Executando NOP")
            pc_counter = last_pc_counter # Mantem

        if self.actionROMAssembly.isChecked():
            rom_line = asm_utils.z01_real_line(self.assembler_task.labels_pos, pc_counter)
        else:
            rom_line = pc_counter

<<<<<<< HEAD
        index = self.romModel.index(rom_line, 0)
        self.romView.setCurrentIndex(index)
        
        print("PROXIMO")
        self.last_step = step

    def update_line_edit(self, line_edit, new_value):
        if line_edit.text() != new_value:
            line_edit.setText(new_value)
            line_edit.setStyleSheet("QLineEdit {background-color: yellow;}")
        else:
            line_edit.setStyleSheet("")


=======
        index = self.rom_model.index(rom_line, 0)
        self.romView.setCurrentIndex(index)

        print("PROXIMO")
        self.last_step = step

    def update_line_edit(self, line_edit, new_value, ignore=False):
        if line_edit.text() != new_value:
            line_edit.setText(new_value)
            if not ignore:
                line_edit.setStyleSheet("QLineEdit {background-color: yellow;}")
            valid = self.valid_binary(line_edit)
            if valid:
                self.on_ram_tooltip(line_edit)
        else:
            line_edit.setStyleSheet("")

>>>>>>> upstream/master
    def valid_rom(self, item):
        if not item.text():
            return None

<<<<<<< HEAD
        if self.actionROMAssembly.isChecked():
            valid = asm_utils.z01_valid_assembly(item.text())
        elif self.actionROMBinario.isChecked():
            valid = self.valid_binary(item.text())
=======
        text = item.text()
        index = item.index()

        while index.row() + 50 >= self.rom_model.rowCount():
            self.rom_model.appendRow(QStandardItem(""))


        if self.actionROMAssembly.isChecked():
            valid = asm_utils.z01_valid_assembly(item.text())
        elif self.actionROMBinario.isChecked():
            valid = self.valid_binary(item)
>>>>>>> upstream/master
        else:
            valid = True

        if valid:
<<<<<<< HEAD
            if (self.actionROMBinario.isChecked() or self.actionROMHexadecimal.isChecked()) and self.editor_converting is False:
                self.actionROMAssembly.setEnabled(False)
            self.changed = True
        else:
            item.setText("")

    def copy_file_to_model(self, file_in, model, preprocessor=None):
        file_in.seek(0, 0)
        for i, l in enumerate(file_in):
            data = l
            if preprocessor is not None:
                data = preprocessor(data)
            model.setItem(i, QStandardItem(data))

    def copy_model_to_file(self, model, f, preprocessor=None):
        f.seek(0, 0)
        for i in range(0, model.rowCount()):
            index = model.index(i, 0)
            data = model.itemFromIndex(index).text().strip()
            if preprocessor is not None:
                data = preprocessor(data)
            f.write(data + "\n")
        f.seek(0, 0)
        return f

    def copy_file_to_file(self, f1, f2, preprocessor=None):
        f1.seek(0, 0)
        f2.seek(0, 0)
        for i, l in enumerate(f1):
            data = l
            if preprocessor is not None:
                data = preprocessor(data)
            f2.write(data)
        f2.seek(0, 0)
        f1.seek(0, 0)
        return f2

=======
            if (self.actionROMBinario.isChecked()) and self.editor_converting is False:
                self.actionROMAssembly.setEnabled(False)
            self.data_changed = True
        else:
            item.setText("")

    def valid_ram(self, item):
        if not item.text():
            return None
        text = item.text()
        index = item.index()

        while index.row() + 100 >= self.ram_model.rowCount():
            self.ram_model.appendRow(QStandardItem("{0:0>16b}".format(0)))

        if text.startswith("d"):
            text = text[1:]
            if text.isdigit():
                item.setText("{0:0>16b}".format(int(text)))

        valid = self.valid_binary(item)

        if valid:
            self.data_changed = True
            self.on_ram_tooltip(item)
        else:
            item.setText("{0:0>16b}".format(0))
>>>>>>> upstream/master

    def assemble(self, callback):
        if self.asm_thread.isRunning() or self.sim_thread.isRunning():
            print("Assembler está sendo executado...")
            return False

        assembler = "java -jar " + self.config_dialog_ui.assemblerLineEdit.text()
        self.assembler_task = AssemblerTask(assembler, "temp/")
<<<<<<< HEAD
        rom_in              = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
        rom_out             = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
        self.copy_file_to_file(self.rom_loaded, rom_in)
=======
        rom_in = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
        rom_out = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
        file_utils.copy_file_to_file(self.rom_stream, rom_in)
>>>>>>> upstream/master
        self.assembler_task.setup(rom_in, rom_out)
        self.assembler_task.finished.connect(callback)
        self.assembler_task.moveToThread(self.asm_thread)
        self.asm_thread.started.connect(self.assembler_task.run)
        self.asm_thread.start()


    def simulate(self, rom_file, ram_file):
        if self.asm_thread.isRunning() or self.sim_thread.isRunning():
            print("Simulador está sendo executado...")
            return False

        self.simulator_task = SimulatorTask("temp/", False, self.config_dialog_ui.simGUIBox.isChecked(), self.config_dialog_ui.rtlLineEdit.text())
<<<<<<< HEAD
        rom_in              = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
        rom_out             = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
        lst_out             = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
=======
        lst_out = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
>>>>>>> upstream/master
        self.simulator_task.setup(rom_file, ram_file, lst_out, self.spinBox.value()*10+10)
        self.simulator_task.finished.connect(self.simulation_end)
        self.simulator_task.moveToThread(self.sim_thread)
        self.sim_thread.started.connect(self.simulator_task.run)
        self.sim_thread.start()
        self.lock_and_show_dialog()

    def lock_and_show_dialog(self):
        ## waits for ASM thread and SIM thread to end
        self.progress_dialog = QProgressDialog("Simulando...", "Cancelar", 0, 0, self.window)
        self.progress_dialog.setCancelButton(None)
        self.progress_dialog.setAutoReset(True)
        self.progress_dialog.setWindowModality(QtCore.Qt.WindowModal)
        self.progress_dialog.setMinimumDuration(0)
        self.progress_dialog.setValue(0)
        self.progress_dialog.setWindowTitle("RESimulatorGUI")
        self.progress_dialog.setWindowFlags(self.progress_dialog.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
<<<<<<< HEAD
        start = QTime.currentTime()
=======
>>>>>>> upstream/master

        while self.asm_thread.isRunning() or self.sim_thread.isRunning():
            qapp.processEvents()

        self.progress_dialog.reset()

    def get_updated_ram(self):
        ram = tempfile.SpooledTemporaryFile(max_size=self.TEMP_MAX_RAM_USE, mode="w+")
<<<<<<< HEAD
        if self.actionRAMHexadecimal.isChecked():
            self.copy_model_to_file(self.ramModel, ram, asm_utils.hex_str_to_bin)
        else:
            self.copy_model_to_file(self.ramModel, ram)
=======
        file_utils.copy_model_to_file(self.ram_model, ram)
>>>>>>> upstream/master
        return ram

    def check_assembler_sucess(self):
        if self.assembler_task is not None and self.assembler_task.success is True:
            return True
<<<<<<< HEAD
        #self.error_dialog = QErrorMessage()
        #self.error_dialog.showMessage("Erro ao traduzir assembly.")
=======
>>>>>>> upstream/master
        QMessageBox.critical(self.window, "Assembler", "Erro ao traduzir assembly.")
        self.step_timer.stop()
        return False

    def assemble_end(self):
        self.asm_thread.quit() # ensure end of thread
        self.asm_thread.wait()
        ram = self.get_updated_ram()
        if not self.check_assembler_sucess():
            return
        print("ASM done!")
        self.simulate(self.assembler_task.stream_out, ram)

    def simulation_end(self):
        self.sim_thread.quit() #ensure end of thread
        self.sim_thread.wait()
        print("SIM done!")
<<<<<<< HEAD
        self.changed = False
=======
        self.data_changed = False
>>>>>>> upstream/master
        self.lst_parser = LSTParser(self.simulator_task.lst_stream)

    def load_converted_asm_bin(self):
        self.asm_thread.quit()
        self.asm_thread.wait()
        if not self.check_assembler_sucess():
            return
<<<<<<< HEAD
        self.copy_file_to_model(self.assembler_task.stream_out, self.romModel)
=======
        file_utils.copy_file_to_model(self.assembler_task.stream_out, self.rom_model)
>>>>>>> upstream/master
        self.editor_converting = False

    def load_converted_asm_hex(self):
        self.asm_thread.quit()
        self.asm_thread.wait()
        if not self.check_assembler_sucess():
            return
<<<<<<< HEAD
        self.copy_file_to_model(self.assembler_task.stream_out, self.romModel, asm_utils.bin_str_to_hex)
=======
        file_utils.copy_file_to_model(self.assembler_task.stream_out, self.rom_model, asm_utils.bin_str_to_hex)
>>>>>>> upstream/master
        self.editor_converting = False

    def valid_binary(self, item):
        valid = True
<<<<<<< HEAD
        text = item.strip()
        if len(text) != 16:
            valid = False
=======
        text = item.text().strip()
>>>>>>> upstream/master

        try:
            val = int(text, 2)
        except ValueError:
            valid = False

        if not valid:
           print("Invalid BIN Instruction: {}".format(item.text()))

        return valid
<<<<<<< HEAD
    
    def clear_simulation(self):
        self.last_step = None
        self.lineEdit_A.setText("0000000000000000")
        self.lineEdit_A.setStyleSheet("")
        self.lineEdit_D.setText("0000000000000000")
        self.lineEdit_D.setStyleSheet("")
        self.lineEdit_S.setText("0000000000000000")
        self.lineEdit_inM.setText("0000000000000000")
        self.lineEdit_inM.setStyleSheet("")
        self.lineEdit_outM.setText("0000000000000000")
        self.lineEdit_outM.setStyleSheet("")
        self.changed = True
        index = self.ramModel.index(0, 0)
        self.ramView.setCurrentIndex(index)
        index = self.romModel.index(0, 0)
        self.romView.setCurrentIndex(index)

    def load_asm(self, filename, model):
        fp  = open(filename, "r")
        self.actionROMAssembly.setChecked(True)
        counter = 0
        for i, l in enumerate(fp):
            if asm_utils.z01_valid_assembly(l.strip()):
                index = self.romModel.index(counter, 0)
                self.romModel.itemFromIndex(index).setText(l.strip())
                counter += 1
        fp.close()

    def load_bin(self, filename, model):
        fp  = open(filename, "r")
        self.actionROMBinario.setChecked(True)
        self.actionROMAssembly.setEnabled(False)
        self.rom_type_sel = self.actionROMBinario
        counter = 0
        for i, l in enumerate(fp):
            if self.valid_binary(l):
                index = self.romModel.index(counter, 0)
                self.romModel.itemFromIndex(index).setText(l.strip())
                counter += 1
        fp.close()

    def resize_event(self):
        newSize = self.lineEdit_A.size().width() + self.label_A.size().width()
        self.label_ALU.setPixmap(self.pixmap_ALU.scaledToWidth(newSize))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Z01 Simulator command line options")
	parser.add_argument("--rtl_dir", default=None)
	args = parser.parse_args()
	qapp = QApplication(sys.argv)
    ##qapp.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
	app = AppMain()
	if args.rtl_dir is not None:
		app.change_rtl_dir(args.rtl_dir)
	app.show()
	sys.exit(qapp.exec_())

=======

    def clear_simulation(self):
        self.last_step = None
        self.update_line_edit(self.lineEdit_A, "0000000000000000", True)
        self.update_line_edit(self.lineEdit_S, "0000000000000000", True)
        self.update_line_edit(self.lineEdit_D, "0000000000000000", True)
        self.update_line_edit(self.lineEdit_inM, "0000000000000000", True)
        self.update_line_edit(self.lineEdit_outM, "0000000000000000", True)
        self.data_changed = True
        index = self.ram_model.index(0, 0)
        self.ramView.setCurrentIndex(index)
        index = self.rom_model.index(0, 0)
        self.romView.setCurrentIndex(index)

    def load_file(self, filename, model):
        fp = open(filename, "r")
        counter = 0
        lines = file_utils.file_len(filename)
        self.rom_model = self.setup_clean_views(self.romView, rows=lines + 200, caption="ROM")
        for i, l in enumerate(fp):
            if asm_utils.z01_valid_assembly(l.strip()):
                index = self.rom_model.index(counter, 0)
                self.rom_model.itemFromIndex(index).setText(l.strip())
                counter += 1
        fp.close()

    def load_asm(self, filename, model):
        self.actionROMAssembly.setChecked(True)
        self.load_file(filename, model)

    def load_bin(self, filename, model):
        self.actionROMBinario.setChecked(True)
        self.actionROMAssembly.setEnabled(False)
        self.load_file(filename, model)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Z01 Simulator command line options")
    parser.add_argument("--rtl_dir", default=None)
    args = parser.parse_args()
    qapp = QApplication(sys.argv)
    app = AppMain()
    if args.rtl_dir is not None:
    	app.change_rtl_dir(args.rtl_dir)
    app.show()
    sys.exit(qapp.exec_())
>>>>>>> upstream/master
