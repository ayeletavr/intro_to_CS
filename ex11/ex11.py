import  copy
from collections import Counter
import itertools
class Node:
    def __init__(self, data, pos=None, neg=None):
        self.data = data
        self.positive_child = pos
        self.negative_child = neg
        self.children = []
        if pos != None:
            self.children.append(pos)
        if neg != None:
            self.children.append(neg)

class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    """Diagnoser is the class that diagnosis a certain tree."""
    def __init__(self, root):
        self.root = root

    def check_if_leaf(self, node):
        """Returns True if specific node is a leaf, otherwise returns False"""
        if not node.positive_child and not node.negative_child:
            return True
        return False

    def diagnose(self, symptoms):
        """
        Gets a list of symptoms and diagnose a specific illness according to the tree.
        :param symptoms: List of symptoms.
        :return: Illness (leaf).
        """
        curr = self.root
        while self.check_if_leaf(curr) == False:
            if curr.data in symptoms:
                curr = curr.positive_child
            else:
                curr = curr.negative_child
        return curr.data


    def calculate_success_rate(self, records):
        """Gets a list of record objects, make a diagnosis to tree and calculates rate of success according to records."""
        success_lst = []
        for record in records:
            diagnosed = self.diagnose(record.symptoms)
            if diagnosed == record.illness:
                success_lst.append(diagnosed)
        success_rate = len(success_lst) / len(records)
        return success_rate


    def return_all_leaves(self):
        """Returns a list contains all leaves of tree."""
        leaves = []
        self.__return_all_leaves(self.root, leaves)
        return leaves

    def __return_all_leaves(self, node, leaves):
        if node is not None:
            if self.check_if_leaf(node):
                leaves.append(node.data)
            for child in node.children:
                self.__return_all_leaves(child, leaves)

    def all_illnesses(self):
        """Returns all illnesses (leafs) in tree."""
        illnesses_lst = self.return_all_leaves()
        illnesses_cnt = Counter()
        for illness in illnesses_lst:
            illnesses_cnt[illness] += 1
        illnesses_cnt = sorted(illnesses_cnt)
        return illnesses_cnt

    def all_max_simple_paths(self):
        """Side function to difference. Returns all paths to leafs it tree."""
        path = []
        all_paths = []
        self.__paths_helper(path).append(all_paths)

    def __paths_helper(self, path):
        path.append(self)
        path_is_maximal = True
        for node in self.root.children:
            if node not in path:
                path_is_maximal = False
                node.__paths_helper(path)
        if path_is_maximal:
            return path
        path.pop()


    def difference(self, other):
        """Gets two diagnosers, returns a list of common symptoms to both trees that diagnosis differen illnesses."""
        curr_lst = self.all_max_simple_paths(root)
        other_lst = self.all_max_simple_paths(other)
        final_lst = []
        for curr_path in curr_lst:
            for other_path in other_lst:
                if curr_path == other_path:
                    return
                for index, curr_node in enumerate(curr_path):
                    for index, other_node in enumerate(other_path):
                        while curr_node[index] == other_node[index]:
                            final_lst.append(curr_node)
                            return final_lst

    def paths_to_illness(self, illness):
        """Gets an illness (str) and finds a path in tree to illness( True = Yes, False = No.)"""
        temp_lst = []
        final_lst = []
        self.__paths_to_illness(illness, temp_lst, final_lst,self.root)
        return final_lst

    def __paths_to_illness(self, illness, path_lst, all_paths,node):
        if not node.negative_child or not node.positive_child:
            if illness == node.data:
                added_lst = copy.deepcopy(path_lst)
                all_paths.append(added_lst)
                return
        else:
            path_lst.append(True)
            self.__paths_to_illness(illness,path_lst,  all_paths, node.positive_child)
            path_lst.pop()
            path_lst.append(False)
            self.__paths_to_illness(illness, path_lst, all_paths, node.negative_child)
            path_lst.pop()

def build_tree(records, symptoms):
    """Gets a list of records and a list of symptoms, and according to this information builds a tree."""

    root_data = symptoms[0]
    pos_data = __build_tree_helper(records, symptoms, 0)
    neg_data = __build_tree_helper(records, symptoms, 0)
    if pos_data is None: #leaf
        for record in records:
            if len(record.symptoms) == len(diagnoser.paths_to_illness(record.illness)[0])\
                    and False not in diagnoser.paths_to_illness(record.illness[0]):
                pos_data = record.illness
                neg_data = pos_data

    root = Node(root_data, Node(pos_data), Node(neg_data))

    return root

def __build_tree_helper(records, symptoms, start):
    pos_and_neg = symptoms[start]
    if start == len(symptoms)-1:
        return pos_and_neg
    __build_tree_helper(records, symptoms, start+1)

def optimal_tree(records, symptoms, depth):
    """This function creates trees and than checks wich one of them has the best success rate. Returns best tree."""
    all_subs = []
    for comb in itertools.combinations(symptoms, depth):
        all_subs.append(comb)
    trees = []
    rates = []
    for comb in all_subs:
        candidate = build_tree(records, comb)
        trees.append(candidate)
        rate_success = diagnoser.calculate_success_rate(records)
        rates.append(rate_success)
    max_rate = max(rates)
    tree_index = rates.index(max_rate)
    return trees[tree_index]


############Tests###############

if __name__ == "__main__":

    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No
    # influenza   cold

    flu_leaf = Node("influenza", None, None)
    cold_leaf = Node("cold", None, None)
    inner_vertex = Node("fever", flu_leaf, cold_leaf)
    healthy_leaf = Node("healthy", None, None)
    root = Node("cough", inner_vertex, healthy_leaf)

    diagnoser = Diagnoser(root)

    # test for 1
    diagnosis = diagnoser.diagnose(["cough"])
    if diagnosis == "cold":
        print("Test 1 passed")
    else:
        print("Test failed. Should have printed cold, printed: ", diagnosis)

    Record3 = Record("influenza", ["cough", "fever"])
    print(diagnoser.diagnose(Record3.symptoms))

    # test for 2
    rate_success = diagnoser.calculate_success_rate(parse_data("tiny_data.txt"))
    if rate_success == 1 / 3:
        print("Test 2 passed")
    else:
        print("test 2 failed.")

    # records = [Record("influenza", ["cough", "fever"]), Record("healthy", []),
    #            Record('hard influenza', ["cougth", "fever", "headache"])]
    # print(diagnoser.calculate_success_rate(records))

    # test for 3
    print(diagnoser.return_all_leaves())
    print(diagnoser.all_illnesses())


    # test for 5
    print(diagnoser.paths_to_illness("influenza"))

    #test for 6
    record1 = Record("influenza", ['cough','fever'])
    record2 = Record('cold', ['cough'])
    records = [record1, record2]
    node = build_tree(records,['fever','influenza'])
    print(node.data)
    print(node.negative_child.data)
    print(node.positive_child.data)
    # print(node.positive_child.da)

    # test for 7
    print(optimal_tree(records, ["cough", "fever"], 1).data)