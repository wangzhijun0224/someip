#_*_coding:utf-8 _*_

'''
fidl基本类型：
参见capicxx-core-tools/docx/CommonAPICppSpecification
fidl类型     ---  commonAPI C++类型
  UInt8      ---     uint8_t
  Int8       ---     int8_t
  UInt16     ---     uint16_t
  Int16      ---     int16_t
  UInt32     ---     uint32_t
  Int32      ---     int32_t
  UInt64     ---     uint64_t
  Int64      ---     int64_t
  Boolean    ---     bool
  Float      ---     float
  Double     ---     double
  String     ---     std::string  (utf8, utf16be, utf16le)
  ByteBuffer ---     std::vector<uint8_t>
-------------------------------------------------------------------------------
commonAPI部署参数：
参见capicxx-core-tools/org.genivi.commonapi.core/deployment/CommonAPI_deployment_spec.fdepl
  interfaces:
    --- DefaultEnumBackingType: {UInt8, UINT16, UInt32, UInt64, Int8, Int16, Int32, Int64} (default: Int32)
  providers:
    *-- ClientInstanceReferences:    Instance[] (optional)
    *-- ProjectVariants: String[] (optional)
  instances:
    *-- Domain:                 String (default: "local")
    --- InstanceId:             String
    *-- DefaultTimeout:         Integer (optional)
    *-- PreregisteredProperties:String[] (optional)  # use "Name=value" as format
    *-- CodeArtifactName:       String (default: "commonapi-gen")
  methods:
    *-- Timeout :   Integer (optional)
    *-- Errors:     String[] (optional)
  attributes:
    *-- Timeout:    Integer (optional)
  enumerations:
    --- EnumBackingType: {UInt8, UINT16, UInt32, UInt64, Int8, Int16, Int32, Int64} (optional)
    *-- ErrorType : { Error, Warning, Info, NoError } (default:Error)
  broadcasts:
    *-- BroadcastType: {signal, error} (default: signal)
    *ErrorName :    String (optional)
-------------------------------------------------------------------------------
CommonAPI-SomeIP部署参数：
参见capicxx-someip-tools/org.genivi.commonapi.someip/deployment/CommonAPI-SOMEIP_deployment_spec.fdepl
  instances:
        SomeIpInstanceID:            Integer                         ;
        SomeIpUnicastAddress:        String                          (default: "");
        SomeIpReliableUnicastPort:   Integer                         (default: 0);
        SomeIpUnreliableUnicastPort: Integer                         (default: 0);
        /*
         * The following three arrays must be used together, meaning the configuration of
         * multicast address and port for an eventgroup is done by setting
         *    SomeIpMulticastEventGroup[X] = <eventgroup identifier>
         *    SomeIpMulticastAddresses[X] = <multicast address for SomeIpMulticastEventGroups[X]>
         *    SomeIpMulticastPorts[X] = <multicast port for SomeIpMulticastEventGroups[X]>
         */
        SomeIpMulticastEventGroups:  Integer[]                       (optional);
        SomeIpMulticastAddresses:    String[]                        (optional);
        SomeIpMulticastPorts:        Integer[]                       (optional);
        /*
         * Define how to retrieve an error message and map it to Franca error parameters
         */
        SomeIpDefaultErrorCoding:    {Header}                        (default: Header);
  interfaces:
        SomeIpServiceID:             Integer                         ;
        SomeIpEventGroups:           Integer[]                       (optional);
  attributes:
        SomeIpGetterID:              Integer                         (optional);
        SomeIpGetterReliable:        Boolean                         (default: false);
        SomeIpGetterPriority:        Integer                         (optional);
        SomeIpSetterID:              Integer                         (optional);
        SomeIpSetterReliable:        Boolean                         (default: false);
        SomeIpSetterPriority:        Integer                         (optional);
        SomeIpNotifierID:            Integer                         (optional);
        SomeIpNotifierReliable:      Boolean                         (default: false);
        SomeIpNotifierPriority:      Integer                         (optional);
        SomeIpNotifierMulticast:     Boolean                         (default: false);
        SomeIpEventGroups:           Integer[]                       (optional);
        SomeIpAttributeEndianess:    {le, be}                        (default: be);
        SomeIpAttributeCRCWidth:     {zero, one, four}               (default: zero);
  methods:
        SomeIpMethodID:              Integer                         ;
        SomeIpReliable:              Boolean                         (default: false);
        SomeIpPriority:              Integer                         (optional);
        /*
         * define how to retrieve an error message and map it to Franca error parameters
         */
        SomeIpErrorCoding:           {Header}                        (default: Header);
        SomeIpMethodEndianess:       {le, be}                        (default: be);
        SomeIpMethodCRCWidth:        {zero, one, four}               (default: zero);
  broadcasts:
        SomeIpEventID:               Integer                         ;
        SomeIpReliable:              Boolean                         (default: false);
        SomeIpPriority:              Integer                         (optional);
        SomeIpMulticast:             Boolean                         (default: false);
        SomeIpEventGroups:           Integer[]                       (optional);

        SomeIpBroadcastEndianess:    {le, be}                        (default: be);
        SomeIpBroadcastCRCWidth:     {zero, one, four}               (default: zero);
  arrays:
        SomeIpArrayMinLength:        Integer                         (default: 0);
        SomeIpArrayMaxLength:        Integer                         (default: 0);
        /* 
         * If SomeIpArrayLengthWidth == 0, the array has SomeIpArrayMaxLength elements.
         * If SomeIpArrayLengthWidth == 1, 2 or 4 bytes, SomeIpArrayMinLength and
         * SomeIpArrayMaxLength are ignored.
         */
        SomeIpArrayLengthWidth:      Integer                         (default: 4);
  unions:
        /*
         * The length field of the union contains the size of the biggest element
         * in the union in bytes;
         * The SomeIpUnionLengthWidth determines the size of the length field;
         * allowed values are 0, 1, 2, 4.
         * 0 means that all types in the union have the same size.
         */
        SomeIpUnionLengthWidth:      Integer                         (optional);
        /*
         * 2^SomeIpUnionTypeWidth*8 different Types in the union.
         */
        SomeIpUnionTypeWidth:        Integer                         (optional);
        /*
         * True means length field before type field, false means length field
         * after type field.
         */
        SomeIpUnionDefaultOrder:     Boolean                         (optional);
        /*
         * If SomeIpUnionLengthWidth == 0, SomeIpUnionMaxLength must be set to the 
         * size of the biggest contained type.
         */
        SomeIpUnionMaxLength:        Integer                         (optional);
  structs:
        /*
         * The length field of the struct contains the size of the struct in bytes;
         * The SomeIpStructLengthWidth determines the size of the length field;
         * allowed values are 0, 1, 2, 4. 0 means that there is no length field.
         */
        SomeIpStructLengthWidth:     Integer                         (default: 0);
  enumerations:
        // Bytes of base type
        SomeIpEnumWidth:             Integer                         (default: 4);
        // Bits to serialize/deserialize
        SomeIpEnumBitWidth:          Integer                         (optional);
        // Invalid value
        SomeIpEnumInvalidValue:		 Integer						 (optional);
  strings:
        SomeIpStringLength:          Integer                         (default: 0);
        /*
         * If LengthWidth == 0, the length of the string has StringLength bytes.
         * If LengthWidth == 1, 2 or 4 bytes, SomeIpStringLength is ignored.
         */
        SomeIpStringLengthWidth:     Integer                         (default: 4);
        /*
         * utf16le LittleEndian, utf16be BigEndian.
         */
        SomeIpStringEncoding:        {utf8, utf16le, utf16be}        (default: utf8);
  byte_buffers:
        SomeIpByteBufferMaxLength:   Integer                        (default: 0);    // 0 means unlimited length
        SomeIpByteBufferMinLength:   Integer                        (default: 0);
  /*
   * From here workaround for missing Franca deployment features.
   */
  attributes:
        SomeIpAttrArrayMinLength:    Integer                         (optional);
        SomeIpAttrArrayMaxLength:    Integer                         (optional);
        SomeIpAttrArrayLengthWidth:  Integer                         (optional);
        SomeIpAttrMapMinLength:      Integer                         (optional);
        SomeIpAttrMapMaxLength:      Integer                         (optional);
        SomeIpAttrMapLengthWidth:    Integer                         (optional);
        SomeIpAttrUnionLengthWidth:  Integer                         (optional);
        SomeIpAttrUnionTypeWidth:    Integer                         (optional);
        SomeIpAttrUnionDefaultOrder: Boolean                         (optional);
        SomeIpAttrUnionMaxLength:    Integer                         (optional);
        SomeIpAttrStructLengthWidth: Integer                         (optional);
        SomeIpAttrEnumWidth:         Integer                         (optional);
        SomeIpAttrEnumBitWidth:      Integer                         (optional);
        SomeIpAttrIntegerBitWidth:   Integer                         (optional);
  arguments:
        SomeIpArgArrayMinLength:      Integer                         (optional);
        SomeIpArgArrayMaxLength:      Integer                         (optional);
        SomeIpArgArrayLengthWidth:    Integer                         (optional);
        SomeIpArgMapMinLength:        Integer                         (optional);
        SomeIpArgMapMaxLength:        Integer                         (optional);
        SomeIpArgMapLengthWidth:      Integer                         (optional);
        SomeIpArgUnionLengthWidth:    Integer                         (optional);
        SomeIpArgUnionTypeWidth:      Integer                         (optional);
        SomeIpArgUnionDefaultOrder:   Boolean                         (optional);
        SomeIpArgUnionMaxLength:      Integer                         (optional);
        SomeIpArgStructLengthWidth:   Integer                         (optional);
        SomeIpArgEnumWidth:           Integer                         (optional);
        SomeIpArgEnumBitWidth:        Integer                         (optional);
        SomeIpArgEnumInvalidValue:    Integer                         (optional);
        SomeIpArgIntegerBitWidth:     Integer                         (optional);
        SomeIpArgIntegerInvalidValue: Integer                         (optional);
  struct_fields:
        SomeIpStructArrayMinLength:      Integer                       (optional);
        SomeIpStructArrayMaxLength:      Integer                       (optional);
        SomeIpStructArrayLengthWidth:    Integer                       (optional);
        SomeIpStructUnionLengthWidth:    Integer                       (optional);
        SomeIpStructUnionTypeWidth:      Integer                       (optional);
        SomeIpStructUnionDefaultOrder:   Boolean                       (optional);
        SomeIpStructUnionMaxLength:      Integer                       (optional);
        SomeIpStructStructLengthWidth:   Integer                       (optional);
        SomeIpStructEnumWidth:           Integer                       (optional);
        SomeIpStructEnumBitWidth:        Integer                       (optional);
        SomeIpStructEnumInvalidValue:    Integer                       (optional);
        SomeIpStructIntegerBitWidth:     Integer                       (optional);
        SomeIpStructIntegerInvalidValue: Integer                       (optional);
  union_fields:
        SomeIpUnionArrayMinLength:    Integer                        (optional);
        SomeIpUnionArrayMaxLength:    Integer                        (optional);
        SomeIpUnionArrayLengthWidth:  Integer                        (optional);
        SomeIpUnionUnionLengthWidth:  Integer                        (optional);
        SomeIpUnionUnionTypeWidth:    Integer                        (optional);
        SomeIpUnionUnionDefaultOrder: Boolean                        (optional);
        SomeIpUnionUnionMaxLength:    Integer                        (optional);
        SomeIpUnionStructLengthWidth: Integer                        (optional);
        SomeIpUnionEnumWidth:         Integer                        (optional);
        SomeIpUnionEnumBitWidth:      Integer                        (optional);
        SomeIpUnionIntegerBitWidth:   Integer                        (optional);
'''

'''
excel格式要求：
    *1. ServiceInstances表的DatatypeReference栏能使用fidl原始类型尽量使用fidl原始类型
    *2. ServiceInstances表的DatatypePackageReference和Package栏内容必须保持一致，可删除DatatypePackageReference栏
    *3. ServiceInstances表的ServiceInterfaceID为SomeIP的服务ID，可放到Deployment表中
    *4. Deployment表中的ServiceInterfaceInstance为SomeIP的instanceID
    *5. ServiceInstances表中参数为数组的，DatatypeReference不使用typedef， 使用'类型[]'(数组格式：[] [startlen-endlen]  [fixlen])
    *6. ServiceInstances表中Eventgroup(Name@EventgroupID)的内容使用'{事件组编号1，事件组编号2, ...}'
    *7. ServiceInstances表中ElementVersion栏去掉，接口有修改，则更新ServiceInterfaceVersion栏,并且记录到History中
    *8. Deployment表中不存放Array, ArrayMax, ArrayMin栏
    *9. ServiceInterfaces和DataTypes表的Packagereference栏删除
    *a. Packages和Deployment表合并,Deployment表中增加Packagereference栏
    *b  Deploymentd的ECU栏删除
'''
from pandas import Series
import pandas as pd

import sys, math

###############################################################################
TAB1_STR = '    '
TAB2_STR = '        '
TAB3_STR = '            '
TAB4_STR = '                '
TAB5_STR = '                    '

string_name_dict = {'utf8':'String', 'utf16be':'String', 'utf16le':'String'}

###############################################################################
service_dict = {}   # 服务字典: servicename -- someip_service

###############################################################################
class someip_service():
    def __init__(self, name, package, serviceid, servicedesc):
        # 以下信息在Deploy表中
        self.name       = name
        self.package    = package
        self.serviceid  = serviceid
        self.description= servicedesc
        self.version    = '1.0' # 扩展数据,暂不使用
        self.deploy_dict={} # 部署字典，key = IP, value = [[instanceID, instanceName, UDPPort, TCPPort]]
                            # 生成部署文件时,仅考虑第一个IP
        # 以下数据在ServiceInterfaces表中        
        self.method_dict={}
        self.field_dict ={}
        self.event_dict ={}
        # 以下信息在DataTypes表中
        self.datatype_dict = {}

    def set_port(self, protocol, port):
        if protocol == 'UDP':
            self.udp_port = port
        elif protocol == 'TCP':
            self.tcp_port = port
        else:
            print('protocol cannot be ', protocol, ' exit!')
            sys.exit(0)

class someip_datatype():
    def __init__(self, name, desc, datatype, data):
        self.name = name
        self.desc = desc
        self.dtype = datatype
        self.data = data

class someip_typedef():
    def __init__(self, datatype):
        self.fidltype = datatype

class someip_enum():
    def __init__(self, datatype):
        self.fidltype = datatype

        self.defaultvalue = ''
        self.value = []
        self.valuedes = []

class someip_struct():
    def __init__(self):
        self.sizelen= 0 
        self.member = []  # someip_para列表

class someip_method():
    def __init__(self, name, id, desc, proto, rettype):
        self.name   = name
        self.id     = id
        self.desc   = desc
        self.proto  = proto
        self.rettype= rettype    # 'RR/FF'
        self.inpara = []
        self.outpara= []

class someip_event():
    def __init__(self, name, groups, id, desc, proto):
        self.name   = name
        self.groups = groups
        self.id     = id
        self.desc   = desc
        self.proto  = proto
        self.inpara = []
        self.outpara= []

class someip_field_item():
    def __init__(self, id, desc, proto, para_type, groups):
        self.id         = id
        self.desc       = desc
        self.proto      = proto
        self.para_type  = para_type
        self.groups     = groups

class someip_field():
    def __init__(self, name):
        self.name       = name
        self.getter     = None  # someip_field_item
        self.setter     = None  # someip_field_item
        self.notifier   = None  # someip_field_item

class someip_para():
    def __init__(self, name, pos, desc, para_type, lenwidth=-1):
        self.name       = name
        self.pos        = pos
        self.desc       = desc
        self.type       = para_type

        self.lenwidth   = lenwidth
        self.isarry     = False
        self.arr_minlen = -1
        self.arr_maxlen = -1
        self.arr_fixlen = -1
        
        arr_start = para_type.find('[')
        if arr_start != -1:
            self.isarry = True
            self.type   = para_type[0:arr_start]
            arrinfo     = para_type[arr_start+1 : para_type.find(']')]
            arrsplit    = arrinfo.split(':')
            if len(arrsplit) == 3:
                if arrsplit[0] != '':
                    self.arr_minlen = int(arrsplit[0])
                if arrsplit[1] != '':
                    self.arr_maxlen = int(arrsplit[1])
                if arrsplit[2] != '':
                    self.lenwidth = int(arrsplit[2])
                if self.arr_minlen != -1 and self.arr_minlen == self.arr_maxlen:  # 仅String支持定长,String不设置数组标志
                    self.arr_fixlen = self.arr_minlen
                    self.isarry     = False
        
###############################################################################
def get_type_name(name):
    if name in string_name_dict:
        return string_name_dict[name]
    else:
        return name

def read_sheet(excel_name, sheet_name, std_columns):
    
    df = pd.read_excel(excel_name, sheet_name)
    # 比较列是否一致
    df_idx_std_columns = pd.Index(std_columns)
    difference = df_idx_std_columns.difference(df.columns, sort=False)
    if difference.size > 0:
        print(sheet_name, ' has no columns: ', difference.values, ' exit!')
        sys.exit(0)
    else:
        print('read ', sheet_name, 'success!')
        # for debug
        diff = df.columns.difference(df_idx_std_columns, sort=False)
        if diff.size > 0:
            print(sheet_name, ' have more columns: ', diff.values)

    return (df)

def check_item_exist(item, check_dict):
    if item in check_dict:
        print(item, ' already in dict, maybe error, please check!!!')
        sys.exit(0)

###############################################################################
def parase_para(item, para_list):
    para_name       = item['ParameterName'].strip()
    if para_name == '-':
        print('skip para name: ', para_name)
        return
    para_pos        = int(item['ParameterPosition'])
    para_dsc        = item['ParameterDescription']
    if type(para_dsc) != type(''): # 剔除NaN
        para_dsc    = ''
    para_type       = item['DatatypeReference'].strip()
    class_para      = someip_para(para_name, para_pos, para_dsc, para_type)
    
    para_list.append(class_para)

def parase_paras(df, inpara, outpara):
    paras_grouped = df.groupby('IN/OUT', sort=False)
    for ps in paras_grouped.groups:
        paras_type  = ps.strip()
        paras_group = paras_grouped.get_group(ps)
        if paras_type == 'IN':
            for index in paras_group.index:
                item = paras_group.loc[index]
                parase_para(item, inpara)
        elif paras_type == 'OUT':
            for index in paras_group.index:
                item = paras_group.loc[index]
                parase_para(item, outpara)
        else: # 无输入输出参数
            print(paras_type, ' is seen as no input and output parameter.')

def parase_method(df, method_dict):
    method_grouped = df.groupby('ElementName', sort=False)
    for m in method_grouped.groups:     #3级, 方法级信息
        method_name         = m.strip()
        print('method name:', method_name)
        check_item_exist(method_name, method_dict)
        method_group        = method_grouped.get_group(m)
        method_first_item   = method_group.loc[method_group.index[0]]
        method_id           = method_first_item['ElementID'].strip()
        method_description  = method_first_item['ElementDescription']
        if type(method_description) != type(''): # 剔除NaN
            method_description = ''
        method_protocol     = method_first_item['UDP/TCP'].strip()
        method_rettype      = method_first_item['RR/FF']
        class_method = someip_method(method_name, method_id, method_description, method_protocol, method_rettype)
        method_dict[method_name] = class_method
        parase_paras(method_group, class_method.inpara, class_method.outpara)

def parase_field(df, field_dict):
    field_grouped = df.groupby('ElementName', sort=False)
    for f in field_grouped.groups:   # 3级,字段级信息
        field_name      = f.strip()
        print('field name: ', field_name)
        check_item_exist(field_name, field_dict)
        class_field     = someip_field(field_name)
        field_dict[field_name] = class_field
        field_group     = field_grouped.get_group(f)
        for index in field_group.index:
            item        = field_group.loc[index]
            field_attr  = item['Setter/Getter/Notifier'].strip()
            field_rettype = item['RR/FF'].strip()
            field_id    = item['ElementID'].strip()
            field_desc  = item['ElementDescription']
            if type(field_desc) != type(''): # 剔除NaN
                field_desc = ''
            field_proto = item['UDP/TCP'].strip()
            field_para_type  = item['DatatypeReference'].strip()
            field_groups = item['Eventgroup']
            if type(field_groups) != type(''): # 剔除NaN
                field_groups = ''
            class_field_item = someip_field_item(field_id, field_desc, field_proto, field_para_type, field_groups)
            if field_attr == 'Getter':
                class_field.getter = class_field_item
            elif field_attr == 'Setter':
                class_field.setter = class_field_item
            elif field_attr == 'Notifier':
                class_field.notifier = class_field_item
            else:
                print('Not support ', field_attr, ' maybe error, please check!!!')
                sys.exit(0)

def parase_event(df, event_dict):
    event_grouped = df.groupby('ElementName', sort=False)
    for e in event_grouped.groups:  # 3级, 事件级信息
        event_name      = e.strip()
        print('event name: ', event_name)
        check_item_exist(event_name, event_dict)
        event_group     = event_grouped.get_group(e)
        event_first_item= event_group.loc[event_group.index[0]]
        event_groups    = event_first_item['Eventgroup'].strip()
        event_rettype   = event_first_item['RR/FF'].strip()
        event_inout     = event_first_item['IN/OUT'].strip()
        if event_rettype != 'FF' or (event_inout != 'OUT' and event_inout != '-'):
            print('event rettype: ', event_rettype, ' event inout: ', event_inout)
            print('event\'s RR/FF or IN/OUT maybe error, please check!!!')
            sys.exit(0)
        event_id        = event_first_item['ElementID'].strip()
        event_desc      = event_first_item['ElementDescription']
        if type(event_desc) != type(''): # 剔除NaN
            event_desc = ''
        event_proto     = event_first_item['UDP/TCP'].strip()
        class_event     = someip_event(event_name, event_groups, event_id, event_desc, event_proto)
        event_dict[event_name] = class_event
        parase_paras(event_group, class_event.inpara, class_event.outpara)

def parase_deploy(filename):
    global service_dict

    # 读取Deployment表信息
    df_deploy   = read_sheet(filename, 'Deployment', 
        [ 'ServiceInterfaceName','ServiceInterfaceID', 'ServiceInterfaceDescription','Packagereference',
         'IP', 'ServiceInstanceID','ServiceInstanceName','L4-Protocol','Port'])
    
    # 解析Deployment信息并放入service_dict中
    service_grouped = df_deploy.groupby('ServiceInterfaceName', sort=False)
    for s in service_grouped.groups:  # 1级: 服务级信息
        print('s: ', s)
        service_name        = s.strip()
        service_group       = service_grouped.get_group(s)
        service_first_item  = service_group.loc[service_group.index[0]]
        service_id          = service_first_item['ServiceInterfaceID'].strip()
        service_desc        = service_first_item['ServiceInterfaceDescription'].strip()
        service_package     = service_first_item['Packagereference'].strip()
        class_service       = someip_service(service_name, service_package, service_id, service_desc)
        service_dict[service_name] = class_service
        
        ip_grouped          = service_group.groupby('IP', sort=False)
        for ip in ip_grouped.groups:    # 2级: IP级信息
            ip_str          = ip.strip()
            ip_group        = ip_grouped.get_group(ip)
            class_service.deploy_dict[ip_str] = []

            instance_grouped    = ip_group.groupby('ServiceInstanceID', sort = False)
            for inst in instance_grouped.groups: # 3级,实例级信息
                instance_id     = inst.strip()
                instance_name   = ''
                udpport         = 0
                tcpport         = 0
                instance_group  = instance_grouped.get_group(inst)
                for index in instance_group.index:
                    item            = instance_group.loc[index]
                    instance_name   = item['ServiceInstanceName'].strip()
                    proto           = item['L4-Protocol'].strip()
                    if proto == 'UDP':
                        udpport     = item['Port']
                    elif proto == 'TCP':
                        tcpport     = item['Port']
                    else:
                        print('Not support L4-Protocol : ', proto , ' please check it!!!')
                        sys.exit(0)
                print([instance_id, instance_name, udpport, tcpport])
                class_service.deploy_dict[ip_str].append([instance_id, instance_name, udpport, tcpport])
    # debug
    for k1 in service_dict:
        print('service name: ', k1)
        item1 = service_dict[k1]
        print('  name:      ', item1.name)
        print('  package:   ', item1.package)
        print('  id:        ', item1.serviceid)
        print('  description:', item1.description)
        print('  version:   ', item1.version)
        deploy_dict = item1.deploy_dict
        for k2 in deploy_dict:
            print('    ip: ', k2)
            for index in range(0, len(deploy_dict[k2])):
                item3 = deploy_dict[k2][index]
                print('      instanceid:    ', item3[0])
                print('      instancename:  ', item3[1])
                print('      udpport:       ', item3[2])
                print('      tcpport:       ', item3[3])
            print('\n')

def parase_service(filename):
    global service_dict

    #读取ServiceInterfaces表信息
    df_service  = read_sheet(filename, 'ServiceInterfaces',
        ['ServiceInterfaceName','Eventgroup', 'Method/Event/Field', 'Setter/Getter/Notifier', 'RR/FF', 'ElementName', 'ElementID', 
         'ElementDescription', 'UDP/TCP', 'IN/OUT', 'ParameterPosition', 'ParameterName','ParameterDescription', 
         'DatatypeReference'])
    
    service_grouped = df_service.groupby('ServiceInterfaceName', sort=False)
    for s in service_grouped.groups:    # 1级, 服务级信息
        service_name = s.strip()
        print('ServiceInterfaceName: ', service_name)   # for debug
        service_group       = service_grouped.get_group(s)
        service_first_item  = service_group.loc[service_group.index[0]]
        if service_name in service_dict:
            class_service                = service_dict[service_name]
        else: # 不处理不在服务字典中的服务
            print(service_name, ' is not in Deploy Sheet， maybe error, please check!!!')
            sys.exit(0)
        category_grouped = service_group.groupby(['Method/Event/Field'], sort=False)
        for c in category_grouped.groups:    # 2级, 方法类别级信息
            category = c.strip()
            print('category: ', category)
            category_group = category_grouped.get_group(c)
            if category == 'Method':
                parase_method(category_group, class_service.method_dict)
            elif category == 'Field':
                parase_field(category_group, class_service.field_dict)
            elif category == 'Event':
                parase_event(category_group, class_service.event_dict)
            else:
                print(category, ' is not a known category, maybe error, please check!!!')
                sys.exit(0)

def value_adjust(value):
    if type(value) != type(1):
        return ('')
    else:
        return (value)

# 暂不支持数组的typedef
def parase_typedef(df_group):
    first_item  = df_group.loc[df_group.index[0]]
    datatype = first_item['DatatypeReference'].strip()
    return someip_typedef(datatype)

def parase_enum(df_group):
    first_item  = df_group.loc[df_group.index[0]]
    datatype = first_item['DatatypeReference'].strip()

    data = someip_enum(datatype)

    for index in df_group.index:
        item = df_group.loc[index]
        value = int(item['Value'])
        value_des = 'E_' + item['ValueDescription'].strip().replace(' ', '_').upper()
        defaultvalue = item['DefaultValue']
        if defaultvalue != '-':
            data.defaulevalue = value_des
        data.value.append(value)
        data.valuedes.append(value_des)
    if data.defaultvalue == '':
        data.defaultvalue = data.valuedes[0]

    return (data)

def parase_member(item, member_list):
    member_name     = item['MemberName'].strip()
    if member_name == '-':
        print('MemberName cannot be -, please check!!!')
        sys.exit(0)
    member_pos      = int(item['MemberPosition'])
    member_dsc      = item['MemberDescription']
    if type(member_dsc) != type(''): # 剔除NaN
        member_dsc  = ''
    member_type     = item['DatatypeReference'].strip()
    member_lensize  = item['DataLenSize']
    if type(member_lensize) != type(''): # 剔除NaN
        member_lensize = -1
    class_member    = someip_para(member_name, member_pos, member_dsc, member_type, member_lensize)
    
    member_list.append(class_member)

def parase_struct(df_group):
    data    = someip_struct()
    start   = 0

    for index in df_group.index:
        item= df_group.loc[index]
        pos = item['MemberPosition']
        if pos == '-':
            data.sizelen = item['DataLenSize']
            continue
        if pos != start:
            print('struct member need to order, please check!!!')
            sys.exit(0)
        parase_member(item, data.member)
        start = start + 1

    return (data)

def parase_union(df_group):
    return (parase_struct(df_group))

def parase_datadefine(name, df_group):
    first_item  = df_group.loc[df_group.index[0]]
    type_desc   = first_item['DatatypeDescription']
    datatype    = first_item['Enum/Typedef/Union/Struct'].strip()
    if datatype == 'Typedef':
        data = parase_typedef(df_group)
    elif datatype == 'Enum':
        data = parase_enum(df_group)
    elif datatype == 'Struct':
        data = parase_struct(df_group)
    elif datatype == 'Union':
        data = parase_union(df_group)
    else:
        print(datatype, ' is unknown type, please check it!!!!')
        sys.exit(0)

    rlt = someip_datatype(name, type_desc, datatype, data)
    return (rlt)

def parase_datatype(filename):
    global service_dict

    # 读取DataTypes表信息
    df_datatype = read_sheet(filename, 'DataTypes',
        ['ServiceInterfaceName', 'DatatypeName', 'DatatypeDescription', 'Enum/Typedef/Union/Struct', 'Value', 'ValueDescription', 
         'DefaultValue', 'MemberPosition', 'MemberName', 'MemberDescription', 'DatatypeReference', 'DataLenSize'])

    service_grouped = df_datatype.groupby('ServiceInterfaceName', sort=False)
    for s in service_grouped.groups:    # 1级, 服务级信息
        service_name        = s.strip()
        print('ServiceInterfaceName: ', service_name)   # for debug
        if service_name in service_dict:
            class_service   = service_dict[service_name]
        else: # 不处理不在服务字典中的服务
            print(service_name, ' is not in Deploy Sheet， maybe error, please check!!!')
            sys.exit(0)
        service_group       = service_grouped.get_group(s)
        datatype_grouped    = service_group.groupby('DatatypeName', sort=False)
        for d in datatype_grouped.groups:    # 2级, 数据类型级信息
            datatype_name   = d.strip()
            print('datatype name: ', datatype_name)
            check_item_exist(datatype_name, class_service.datatype_dict)
            datatype_group  = datatype_grouped.get_group(d)
            datadef         = parase_datadefine(datatype_name, datatype_group)
            class_service.datatype_dict[datatype_name] = datadef

def hexstr2decstr(hexstr):
    return (str(int(hexstr, 16)) + '  //' + hexstr)

def write_argtype_fdepl(fdeplfile, inout, written):
    if written == False:
        fdeplfile.write(TAB2_STR + inout + ' {\n')
        return (True)
    return (True)

def check_need_write_arg_fdepl(para):
    para_type = get_type_name(para.type)
    if para_type == 'String': # 字符串判断
        if para.type[3] != '8' or para.arr_fixlen != -1 or para.lenwidth != -1:
            return True
        else:
            return False
    elif para.isarry == True:   # 数组判断
            if para.arr_minlen != -1 or para.arr_maxlen != -1 or para.lenwidth != -1:
                return True
            else:
                return False
    else:
        return False

def write_arg_fdepl(fdeplfile, para, inout, written):
    para_type = get_type_name(para.type)
    if check_need_write_arg_fdepl(para) == True:
        written = write_argtype_fdepl(fdeplfile, inout, written)
        fdeplfile.write(TAB3_STR + para.name + '{\n')
        if para_type == 'String':
            if para.type[3] != '8':
                fdeplfile.write(TAB4_STR + 'SomeIpStringEncoding = ' + para.type + '\n')
            if para.arr_fixlen != -1:
                fdeplfile.write(TAB4_STR + 'SomeIpStringLength = ' + str(para.arr_fixlen) + '\n')
            if para.lenwidth != -1:
                fdeplfile.write(TAB4_STR + 'SomeIpStringLengthWidth = ' + str(para.lenwidth) + '\n')
        else:
            if para.arr_minlen != -1:
                fdeplfile.write(TAB4_STR + 'SomeIpArgArrayMinLength = ' + str(para.minlen) + '\n')
            if para.arr_maxlen != -1:
                fdeplfile.write(TAB4_STR + 'SomeIpArgArrayMaxLength = ' + str(para.arr_maxlen) + '\n')
            if para.lenwidth != -1:
                fdeplfile.write(TAB4_STR + 'SomeIpArgArrayLengthWidth = ' + str(para.lenwidth) + '\n')
        fdeplfile.write(TAB3_STR + '}\n')
    return written

def write_args(wFile, wFile2, paras, inout):
    if len(paras) > 0:
        wFile.write(TAB2_STR + inout + ' {\n')   # write para begin
        written_args_fdepl = False
        for index in range(0, len(paras)):
            para = paras[index]
            para_type = get_type_name(para.type)
            if para.isarry == True:
                para_type = para_type + '[]'
            wFile.write(TAB3_STR + para_type + ' ' + para.name + ' //' + str(index) + '\n')
            written_args_fdepl = write_arg_fdepl(wFile2, para, inout, written_args_fdepl)
        if written_args_fdepl == True:
            wFile2.write(TAB2_STR + '}\n')
        wFile.write(TAB2_STR + '}\n')   # write para end

def write_event(wFile, wFile2, event_dict):
    for e in event_dict:
        event       = event_dict[e]
        event_name  = event.name
        event_id    = event.id
        event_proto = event.proto
        event_groups= event.groups
        inparas     = event.inpara
        outparas    = event.outpara
        line        = TAB1_STR + 'broadcast ' + event_name + ' {\n'
        wFile.write(line)       # write event to fidl start
        wFile2.write(line)      # write event to fdepl start
        wFile2.write(TAB2_STR + 'SomeIpEventID = ' + hexstr2decstr(event_id) + '\n') # write SomeIpEventID to fdepl
        if event_proto == 'TCP':
            wFile2.write(TAB2_STR + 'SomeIpReliable = true\n')         # write SomeIpReliable to fdepl
        if event_groups != '':
            wFile2.write(TAB2_STR + 'SomeIpEventGroups = ' + event_groups + '\n') # write SomeIpEventGroups to fdepl
        if len(inparas) > 0:
            print('event must have no in para, maybe error, please check!!!')
            sys.exit(0)
        write_args(wFile, wFile2, outparas, 'out')
        wFile.write(TAB1_STR + '}\n')   # write event to fidl end
        wFile2.write(TAB1_STR + '}\n')   # write event to fdepl end

def write_field(wFile, wFile2, field_dict):
    for f in field_dict:
        field       = field_dict[f]
        field_name  = field.name
        field_getter= field.getter
        line        = TAB1_STR + 'attribute ' + field_getter.para_type + ' ' + field_name
        if field.setter is None:
            line    = line + ' readonly'
        line        = line + '\n'
        wFile.write(line)
        # write fdepl start
        wFile2.write(TAB1_STR + 'attribute ' + field_name + ' {\n')
        if field.getter is not None:
            f_id    = field.getter.id
            f_proto = field.getter.proto
            wFile2.write(TAB2_STR + 'SomeIpGetterID = ' + hexstr2decstr(f_id) + '\n')
            if f_proto == 'TCP':
                wFile2.write(TAB2_STR + 'SomeIpGetterReliable = true\n')
        if field.setter is not None:
            f_id    = field.setter.id
            f_proto = field.setter.proto
            wFile2.write(TAB2_STR + 'SomeIpSetterID = ' + hexstr2decstr(f_id) + '\n')
            if f_proto == 'TCP':
                wFile2.write(TAB2_STR + 'SomeIpSetterReliable = true\n')
        if field.notifier is not None:
            f_id    = field.notifier.id
            f_proto = field.notifier.proto
            f_groups= field.notifier.groups
            wFile2.write(TAB2_STR + 'SomeIpNotifierID = ' + hexstr2decstr(f_id) + '\n')
            if f_proto == 'TCP':
                wFile2.write(TAB2_STR + 'SomeIpNotifierReliable = true\n')
            if f_groups != '':
                wFile2.write(TAB2_STR + 'SomeIpEventGroups = ' + f_groups + '\n')
        # write fdepl end
        wFile2.write(TAB1_STR + '}\n')

def write_method(wFile, wFile2, method_dict):
    for m in method_dict:
        method          = method_dict[m]
        method_name     = method.name
        method_rettype  = method.rettype
        method_id       = method.id
        method_proto    = method.proto
        line = TAB1_STR + 'method ' + method_name
        if method_rettype == 'FF':
            line = line + ' fireAndForget {\n'
        else:
            line = line + ' {\n'
        wFile.write(line)                                           # write method to fidl start
        wFile2.write(TAB1_STR + 'method ' + method_name + ' {\n')   # write method to fdepl start
        wFile2.write(TAB2_STR + 'SomeIpMethodID = ' + hexstr2decstr(method_id) + '\n')
        if method_proto == 'TCP':
            wFile2.write(TAB2_STR + 'SomeIpReliable = true\n')
        method_inpara = method.inpara
        if len(method_inpara) > 0:
            write_args(wFile, wFile2, method_inpara, 'in')

        method_outpara = method.outpara
        if len(method_outpara) > 0:
            write_args(wFile, wFile2, method_outpara, 'out')
        
        wFile.write(TAB1_STR + '}\n')   # write method to method end
        wFile2.write(TAB1_STR + '}\n')  # write method to fdepl end

def write_datatype(wFile, wFile2, datatype_dict):
    for d in datatype_dict:
        datatype    = datatype_dict[d]
        dt_name     = datatype.name
        dt_desc     = datatype.desc
        dt_dtype    = datatype.dtype
        dt_data     = datatype.data
        written_head = False
        if dt_dtype == 'Typedef':
            wFile.write(TAB1_STR + 'typedef ' + dt_name + ' is ' + dt_data.fidltype + '\n')
        elif dt_dtype == 'Enum':
            wFile.write(TAB1_STR + 'enumeration ' + dt_name + ' {\n') # write enum to fidl start
            for index in range(0, len(dt_data.valuedes)):
                wFile.write(TAB2_STR + dt_data.valuedes[index] + ' = ' + str(dt_data.value[index]) + '\n')
            wFile.write(TAB1_STR + '}\n')  # write enum to fidl end
        elif dt_dtype == 'Struct' or dt_dtype == 'Union':
            wFile.write(TAB1_STR + dt_dtype.lower() + ' ' + dt_name + ' {\n') # write struct/union to fidl start
            
            if dt_data.sizelen != 0:
                written_head = True
                wFile2.write(TAB1_STR + dt_dtype.lower() + ' ' + dt_name + ' {\n')
                wFile2.write(TAB2_STR + 'SomeIp' + dt_dtype + 'LengthWidth = ' + str(dt_data.sizelen) + '\n')
                if dt_dtype == 'Union':
                    wFile2.write(TAB2_STR + 'SomeIp' + dt_dtype + 'TypeWidth = ' + str(dt_data.sizelen) + '\n')
            for index in range(0, len(dt_data.member)):
                member = dt_data.member[index]
                mem_type = get_type_name(member.type)
                if member.isarry == True:
                    wFile.write(TAB2_STR + mem_type + '[] ' + member.name + '\n')
                else:
                    wFile.write(TAB2_STR + mem_type + ' ' + member.name + '\n')
                # write member fdepl
                if dt_data.sizelen != 0:
                    if mem_type in datatype_dict:   # 成员本身是复合结构
                        mem_type = datatype_dict[mem_type].dtype

                    if mem_type == 'Struct' or mem_type == 'Union':
                        wFile2.write(TAB2_STR + member.name + '{\n')
                        wFile2.write(TAB3_STR + 'SomeIp'+ dt_dtype + mem_type+'LengthWidth = ' + str(dt_data.sizelen) + '\n')
                        wFile2.write(TAB2_STR + '}\n')
                    elif member.isarry == True:
                        wFile2.write(TAB2_STR + member.name + '{\n')
                        wFile2.write(TAB3_STR + 'SomeIp'+ dt_dtype +'ArrayLengthWidth = ' + str(dt_data.sizelen) + '\n')
                        wFile2.write(TAB2_STR + '}\n')
                    elif mem_type == 'String':
                        wFile2.write(TAB2_STR + member.name + '{\n')
                        wFile2.write(TAB3_STR + 'SomeIp' +'StringLengthWidth = ' + str(dt_data.sizelen) + '\n')
                        if member.type[3] != '8': # not utf8
                            wFile2.write(TAB3_STR + 'SomeIp' +'StringEncoding = ' + member.type + '\n')
                        wFile2.write(TAB2_STR + '}\n')
                else:
                    if mem_type == 'String' and member.type[3] != '8':
                        if written_head != True:
                            written_head = True
                            wFile2.write(TAB1_STR + dt_dtype.lower() + ' ' + dt_name + ' {\n')
                        wFile2.write(TAB2_STR + member.name + '{\n')
                        wFile2.write(TAB3_STR + 'SomeIp' +'StringEncoding = ' + member.type + '\n')
                        wFile2.write(TAB2_STR + '}\n')
            wFile.write(TAB1_STR+'}\n') # write struct  to fidl end
            if written_head == True:
                wFile2.write(TAB1_STR + '}\n')
        else:
            print(dt_type, ' is unknown type, please check it!!!')
            sys.exit(0)

'''
检查是否有属于commonAPI的基本部署，检查项:
  1. 枚举是否有非Int32类型
'''
def check_common_deploy(datatype_dict):
    depl_dict = {}
    for d in datatype_dict:
        datatype    = datatype_dict[d]
        dt_name     = datatype.name
        dt_desc     = datatype.desc
        dt_dtype    = datatype.dtype
        dt_data     = datatype.data
        if dt_dtype == 'Enum':
            if dt_data.fidltype != 'UInt32':
                depl_dict[d] = datatype
    return(depl_dict)

def create_file():
    global service_dict

    for s in service_dict:
        service         = service_dict[s]
        service_name    = service.name
        fidlfile_name   = './fidl/'+service_name + '.fidl'
        fidlfile        = open(fidlfile_name, 'w')
        fdeplfile_name  = './fidl/'+service_name + '.fdepl'
        fdeplfile       = open(fdeplfile_name, 'w')
        # write license declare
        wline = '/* This Source Code Form is subject to the terms of the Mozilla Public\n'     \
              + ' * License, v. 2.0. If a copy of the MPL was not distributed with this\n'     \
              + ' * file, You can obtain one at http://mozilla.org/MPL/2.0/. */\n\n'
        fidlfile.write(wline)
        fdeplfile.write(wline)
        # write package name to fidl
        wline = 'package ' + service.package + '\n\n' 
        fidlfile.write(wline)
        # write interface(service) to fidl begin
        wline = 'interface ' + service_name + ' {\n\n'
        fidlfile.write(wline)
        # write service version to fidl
        service_version = service.version
        version_major = service_version.split('.')[0]
        version_minor = service_version.split('.')[1]
        wline = '    version { major ' +  version_major + ' minor ' + version_minor + ' }\n\n'
        fidlfile.write(wline)
        # write import to fdepl
        common_depl_dict = check_common_deploy(service.datatype_dict)
        if len(common_depl_dict) > 0:
            fdeplfile.write('import \"platform:/plugin/org.genivi.commonapi.core/deployment/CommonAPI_deployment_spec.fdepl\"\n')
        fdeplfile.write('import \"platform:/plugin/org.genivi.commonapi.someip/deployment/CommonAPI-SOMEIP_deployment_spec.fdepl\"\n')
        fdeplfile.write('import \"' + service_name + '.fidl\"\n\n')
        # write common depl to fdepl
        if len(common_depl_dict) > 0:
            fdeplfile.write('define org.genivi.commonapi.core.deployment for interface ' + service.package + '.' + service_name + ' {\n')
            for d in common_depl_dict:
                enum_name = common_depl_dict[d].name
                enum_type = common_depl_dict[d].data.fidltype
                fdeplfile.write(TAB1_STR + 'enumeration ' + enum_name + '{\n')
                fdeplfile.write(TAB2_STR + 'EnumBackingType = ' + enum_type + '\n')
                fdeplfile.write(TAB1_STR + '}\n')
            fdeplfile.write('}\n\n')
        # write someip depl to fdepl begin
        fdeplfile.write('define org.genivi.commonapi.someip.deployment for interface ' + service.package + '.' + service_name + ' {\n')
        fdeplfile.write(TAB1_STR + 'SomeIpServiceID = ' + hexstr2decstr(service.serviceid) + '\n\n')
        # write attribute(field)
        write_field(fidlfile, fdeplfile, service.field_dict)
        fidlfile.write('\n')
        fdeplfile.write('\n')
        # write method
        write_method(fidlfile, fdeplfile, service.method_dict)
        fidlfile.write('\n')
        fdeplfile.write('\n')
        # write broacast(event)
        write_event(fidlfile, fdeplfile, service.event_dict)
        fidlfile.write('\n')
        fdeplfile.write('\n')
        # write datatype
        write_datatype(fidlfile, fdeplfile, service.datatype_dict)
        fidlfile.write('\n')
        fdeplfile.write('\n')

        # write service end
        fidlfile.write('}\n')
        fidlfile.close()
        
        fdeplfile.write('}\n\n') # write someip depl to fdepl end
        # write provider to fdepl, 只写第一个ip的部署信息
        deploy_dict = service.deploy_dict
        start = 0
        for ip in deploy_dict:
            if start != 0:
                break
            start = 1
            fdeplfile.write('define org.genivi.commonapi.someip.deployment for provider ' + service_name + ' {\n')
            for index in range(0, len(deploy_dict[ip])):
                item            = deploy_dict[ip][index]
                instance_id     = item[0]
                instance_name   = item[1]
                instance_udp    = item[2]
                instance_tcp    = item[3]
                fdeplfile.write(TAB1_STR + 'instance ' + service.package + '.' + service_name  + ' {\n')
                fdeplfile.write(TAB2_STR + 'InstanceId = \"' + instance_name + '\"\n')
                fdeplfile.write(TAB2_STR + 'SomeIpInstanceID = ' + hexstr2decstr(instance_id) + '\n')
                fdeplfile.write(TAB2_STR + 'SomeIpReliableUnicastPort = ' + str(instance_udp) + '\n')
                fdeplfile.write(TAB2_STR + 'SomeIpUnreliableUnicastPort = ' + str(instance_tcp) + '\n')
                fdeplfile.write(TAB1_STR + '}\n')
            fdeplfile.write('}\n')
        fdeplfile.close()


###############################################################################
if __name__ == "__main__":

    #xlsx_name = sys.argv[1]
    #xlsx_names = ['./doc/SOMEIP_Static_InterfaceDescription_1v9_20190430.xlsx']
    #xlsx_names = ['./doc/SOMEIP_ETS_Demo.xlsx']
    #'''
    xlsx_names = ['./doc/SOMEIP_templete.xlsx' #,
        #'./doc/M01_Ethernet_communication_SOMEIP_Static_InterfaceDescription_0v4_Draft_2018.05.10.xlsx',
        #'./doc/M01_Ethernet_communication_SOMEIP_Static_InterfaceDescription_0v4_Draft_2018.05.24.xlsx',
        #'./doc/SOMEIP_ETS_Demo.xlsx',
        #'./doc/SOMEIP_Static_InterfaceDescription_SomeIP-for-test_1012.xlsx',
        #'./doc/SOMEIP_Static_InterfaceDescription_0v5.xlsx',
        #'./doc/SOMEIP_Static_InterfaceDescription_0v5_20181024.xlsx',
        #'./doc/SOMEIP_Static_InterfaceDescription_0v6_20181214.xlsx',
        #'./doc/SOMEIP_Static_InterfaceDescription_1v8_20190203.xlsx',
        #'./doc/SOMEIP_Static_InterfaceDescription_1v9_20190430.xlsx'
        ]
    #'''

    for xlsx_name in xlsx_names:
        print("excel file name: ", xlsx_name)
        service_dict = {}
        parase_deploy(xlsx_name)
        parase_service(xlsx_name)
        parase_datatype(xlsx_name)

        create_file()

        '''
        print('\n\n\n*********\n\n')
        for key in package_dict:
            print(key)
            print(package_dict[key].name)
        '''