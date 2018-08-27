/* Automatically generated nanopb header */
/* Generated by nanopb-0.4.0-dev at Tue Jul  3 12:58:21 2018. */

#ifndef PB_AIRCENSELORA_PB_H_INCLUDED
#define PB_AIRCENSELORA_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _airCenseProto {
    float NO2;
    float CO;
    float temperature;
    float humidity;
    int32_t CO2;
    float PM2_5;
    float PM10;
/* @@protoc_insertion_point(struct:airCenseProto) */
} airCenseProto;

/* Default values for struct fields */

/* Initializer values for message structs */
#define airCenseProto_init_default               {0, 0, 0, 0, 0, 0, 0}
#define airCenseProto_init_zero                  {0, 0, 0, 0, 0, 0, 0}

/* Field tags (for use in manual encoding/decoding) */
#define airCenseProto_NO2_tag                    1
#define airCenseProto_CO_tag                     2
#define airCenseProto_temperature_tag            3
#define airCenseProto_humidity_tag               4
#define airCenseProto_CO2_tag                    5
#define airCenseProto_PM2_5_tag                  6
#define airCenseProto_PM10_tag                   7

/* Struct field encoding specification for nanopb */
extern const pb_field_t airCenseProto_fields[8];

/* Maximum encoded size of messages (where known) */
#define airCenseProto_size                       41

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define AIRCENSELORA_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif