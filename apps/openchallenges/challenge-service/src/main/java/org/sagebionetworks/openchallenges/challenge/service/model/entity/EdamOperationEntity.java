package org.sagebionetworks.openchallenges.challenge.service.model.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "edam_concept")
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class EdamOperationEntity {

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  @Column(nullable = false, updatable = false)
  private Long id;

  @Column(name = "class_id", nullable = false)
  private String classId;

  @Column(name = "preferred_label", nullable = false)
  private String preferredLabel;
}